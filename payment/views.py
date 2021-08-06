from decimal import Decimal

from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from orders.models import Order, OrderItem
from .ecpay_payment import process as ecpay_process
from datetime import datetime

from shop.tools import get_product_string
from .payment import save_ecpay_return

def ecpay_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = 'http://'+request.get_host()
    order_items = OrderItem.objects.filter(order=order)
    products = get_product_string(order_items)
    order_params = {
        'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
        'StoreID': '',
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        'PaymentType': 'aio',
        'TotalAmount': str(order.get_total_cost()),
        'TradeDesc': '訂單測試',
        'ItemName': products,
        'ReturnURL': host+reverse('payment:ecpay_return'),
        'ChoosePayment': 'ALL',
        'ClientBackURL': 'https://www.ecpay.com.tw/client_back_url.php',
        'ItemURL': 'https://www.ecpay.com.tw/item_url.php',
        'Remark': '交易備註',
        'ChooseSubPayment': '',
        # 'OrderResultURL': reverse('payment:order_result'),
        'NeedExtraPaidInfo': 'Y',
        'DeviceSource': '',
        'IgnorePayment': '',
        'PlatformID': '',
        'InvoiceMark': 'N',
        'CustomField1': str(order_id),
        'CustomField2': '',
        'CustomField3': '',
        'CustomField4': '',
        'EncryptType': 1,
    }


    extend_params_1 = {
    'ExpireDate': 7,
    'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
    'ClientRedirectURL': '',
}

    extend_params_2 = {
    'StoreExpireDate': 15,
    'Desc_1': '',
    'Desc_2': '',
    'Desc_3': '',
    'Desc_4': '',
    'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
    'ClientRedirectURL': '',
}

    extend_params_3 = {
    'BindingCard': 0,
    'MerchantMemberID': '',
}

    extend_params_4 = {
    'Redeem': 'N',
    'UnionPay': 0,
}

    inv_params = {
    # 'RelateNumber': 'Tea0001', # 特店自訂編號
    # 'CustomerID': 'TEA_0000001', # 客戶編號
    # 'CustomerIdentifier': '53348111', # 統一編號
    # 'CustomerName': '客戶名稱',
    # 'CustomerAddr': '客戶地址',
    # 'CustomerPhone': '0912345678', # 客戶手機號碼
    # 'CustomerEmail': 'abc@ecpay.com.tw',
    # 'ClearanceMark': '2', # 通關方式
    # 'TaxType': '1', # 課稅類別
    # 'CarruerType': '', # 載具類別
    # 'CarruerNum': '', # 載具編號
    # 'Donation': '1', # 捐贈註記
    # 'LoveCode': '168001', # 捐贈碼
    # 'Print': '1',
    # 'InvoiceItemName': '測試商品1|測試商品2',
    # 'InvoiceItemCount': '2|3',
    # 'InvoiceItemWord': '個|包',
    # 'InvoiceItemPrice': '35|10',
    # 'InvoiceItemTaxType': '1|1',
    # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
    # 'DelayDay': '0', # 延遲天數
    # 'InvType': '07', # 字軌類別
}
    return HttpResponse(ecpay_process(order_params, inv_params))

@csrf_exempt
def ecpay_return(request):
    result = ''
    if request.method == 'POST':
        order_id = request.POST['CustomField1']
        form_data = request.POST.copy()
        form_data['order'] = order_id
        result = save_ecpay_return(form_data)
    return HttpResponse(result)


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
