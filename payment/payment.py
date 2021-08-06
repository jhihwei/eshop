from .models import Ecpay_Payment
from .forms import Ecpay_Return_Form

def save_ecpay_return(form_data):
    form = Ecpay_Return_Form(form_data)
    if form.is_valid():
        result = form.save()
    else:
        print(form.errors)
        return form.errors