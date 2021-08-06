from django.urls import path, re_path
from . import views
urlpatterns = [
    # ecpay
    path('ecpay_return', views.ecpay_return, name='ecpay_return'),
    path('order_result', views.payment_done, name='order_result'),
    path('ecpay', views.ecpay_payment, name='ecpay_payment'),
    # ecpay end
    re_path(r'^canceled/$', views.payment_canceled, name='canceled'),
]
