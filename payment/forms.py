from django import forms
from .models import Ecpay_Payment
from django.utils.translation import gettext_lazy as _


class Ecpay_Return_Form(forms.ModelForm):

    class Meta:
        model = Ecpay_Payment
        fields = ['MerchantID', 'MerchantTradeNo', 'RtnCode',
                  'TradeNo', 'TradeAmt', 'PaymentDate', 'order']
        labels = {'order':'CustomField1',}