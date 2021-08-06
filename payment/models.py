from django.db import models
from orders.models import Order
class Ecpay_Payment(models.Model):
    MerchantID = models.CharField(null=False, verbose_name='特店編號', max_length=30)
    MerchantTradeNo = models.CharField(null=False, verbose_name='特店交易編號', max_length=30)
    RtnCode = models.IntegerField(null=False, verbose_name='交易狀態')
    TradeNo = models.CharField(null=False, verbose_name='綠界交易編號', max_length=30)
    TradeAmt = models.IntegerField(null=False, verbose_name='交易金額')
    PaymentDate = models.DateTimeField()
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE, default=0)

    
    class Meta:
        verbose_name = '綠界訂單'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id