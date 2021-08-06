from django.urls import path, re_path
from . import views
urlpatterns = [
    # ecpay
    path('register', views.register, name='register'),
]