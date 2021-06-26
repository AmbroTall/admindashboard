from django import forms
from django.forms import ModelForm
from . models import Customer,Order, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registerform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')



class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'email', 'phone')


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer','product', 'status')
        widget = {
            'status':forms.ChoiceField()
        }

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','category', 'price')

        widget = {
            'category': forms.ChoiceField()
        }