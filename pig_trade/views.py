from django.shortcuts import render
from pig_trade import models
from pig_trade import forms
import pandas as pd
# Create your views here.

def Orders(request):
    if request.method == 'POST':
        order_form = forms.OrderForm(request.POST)
        if order_form.is_valid():
            name = order_form.cleaned_data.get('username')
            phone = order_form.cleaned_data.get('phone')
            email = order_form.cleaned_data.get('email')
            avg_weight = order_form.cleaned_data.get('avg_weight')
            number = order_form.cleaned_data.get('number')
            order = models.Order
            order.agent = name
            order.phone = phone
            order.avg_weight = avg_weight
            order.email = email
            order.save()
            y = pd.Dataframe()
            return render(request, 'pig_trade/confirm.html', locals())
    else:
        orders_form = forms.OrderForm()
        return render(request, 'pig_trade/order.html', locals())

