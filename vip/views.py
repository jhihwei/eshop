from django.shortcuts import render
from vip.models import VIP_User
from .forms import VIPRegisterForm
def register(request):
    form = VIPRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'shop_v2/vip.html')
    else:
        return render(request, 'vip/register.html')

