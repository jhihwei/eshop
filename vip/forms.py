from django import forms

from .models import VIP_User


class VIPRegisterForm(forms.ModelForm):
    class Meta:
        model = VIP_User
        fields = ['name', 'line_id']
