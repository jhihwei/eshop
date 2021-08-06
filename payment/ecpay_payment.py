import hashlib
from urllib import parse
import collections
from dotenv import load_dotenv
import os
from datetime import datetime
import importlib.util
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk",
    "payment/ecpay_payment_sdk.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
load_dotenv()

params = {}

if os.getenv('web_type') == 'offical':
    # 正式環境
    params = {
        'MerchantID': 'ID隱藏',
        'HashKey': 'Key 隱藏',
        'HashIV': 'IV 隱藏',
        'action_url':
        'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5'
    }
else:
    # 測試環境
    params = {
        'MerchantID': '2000132',
        'HashKey': '5294y06JbISpM5x9',
        'HashIV': 'v77hoKGq4kWxNNIS',
        'action_url': 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'
    }


def get_mac_value(cls, get_request_form):

    params = dict(get_request_form)
    if params.get('CheckMacValue'):
        params.pop('CheckMacValue')

    ordered_params = collections.OrderedDict(
        sorted(params.items(), key=lambda k: k[0].lower()))

    HahKy = cls().params['HashKey']
    HashIV = cls().params['HashIV']

    encoding_lst = []
    encoding_lst.append('HashKey=%s&' % HahKy)
    encoding_lst.append(''.join([
        '{}={}&'.format(key, value)
        for key, value in ordered_params.items()
    ]))
    encoding_lst.append('HashIV=%s' % HashIV)

    safe_characters = '-_.!*()'

    encoding_str = ''.join(encoding_lst)
    encoding_str = parse.quote_plus(str(encoding_str),
                                    safe=safe_characters).lower()

    check_mac_value = ''
    check_mac_value = hashlib.sha256(
        encoding_str.encode('utf-8')).hexdigest().upper()

    return check_mac_value


def process(order_params, inv_params):
    # 建立實體
    ecpay_payment_sdk = module.ECPayPaymentSdk(
        MerchantID='2000132',
        HashKey='5294y06JbISpM5x9',
        HashIV='v77hoKGq4kWxNNIS'
    )
    # 合併延伸參數
    # order_params.update(extend_params_1)
    # order_params.update(extend_params_2)
    # order_params.update(extend_params_3)
    # order_params.update(extend_params_4)
    # 合併發票參數
    order_params.update(inv_params)

    try:
        # 產生綠界訂單所需參數
        final_order_params = ecpay_payment_sdk.create_order(order_params)

        # 產生 html 的 form 格式
        action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'  # 測試環境
        # action_url = 'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5' # 正式環境
        html = ecpay_payment_sdk.gen_html_post_form(
            action_url, final_order_params)
        return html
    except Exception as error:
        print('An exception happened: ' + str(error))
