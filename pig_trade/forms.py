from django import forms

class OrderForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    avg_weight = forms.CharField(label="均重", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    avg_weight_price = forms.CharField(label="均价", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
