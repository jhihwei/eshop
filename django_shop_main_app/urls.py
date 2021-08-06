"""django_shop_main_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # CKEDITOR
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # paypal
    # path('paypal/', include('paypal.standard.ipn.urls')),

    # eshop
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls','cart'), namespace='cart')),
    path('orders/', include(('orders.urls','orders'), namespace='orders')),
    path('payment/', include(('payment.urls','payment'), namespace='payment')),
    path('', include(('shop.urls', 'shop'), namespace='shop')),
    path('vip/', include(('vip.urls', 'vip'), namespace='vip')),
    
    # django-allauth網址
    path('accounts/', include('allauth.urls')), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
