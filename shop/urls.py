from django.urls.conf import include
from shop.views import product_list
from django.urls import path, re_path
from . import views
from payment import urls as payment_urls


urlpatterns = [
    path('payment', include(payment_urls)),
    re_path(r'category', views.category_list, name='category_list'),
    re_path(r'content/(?P<slug>[a-zA-Z0-9-]+)/$',
            views.page_content, name='page_content'),
    re_path(r'category/(?P<category_name>[a-zA-Z0-9-]+)/$',
            views.product_list, name='category'),
    path('', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
            views.product_list, name='product_list_by_category'),
    path('vip/<str:vip_class>/', views.product_list, name='vip_product_list'),
    path('spec/vip', views.vip, name='vip'),
    re_path(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/$',
            views.product_detail, name='product_detail'),
    re_path(r'^(?P<product_id>\d+)/(?P<slug>[-\w]+)/(?P<vip_class>[-\w]+)$',
            views.product_detail, name='vip_product_detail'),

]
