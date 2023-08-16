from django import forms
from .models import Customer, Item

class AddNewCustomer(forms.ModelForm):
    # first_name = forms.CharField(max_length= 30)
    # last_name = forms.CharField(max_length= 30)
    # email = forms.EmailField()
    # description = forms.CharField(max_length= 220)

    class Meta:
        model = Customer
        fields = ['name', 'address' ]


class AddNewItem(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['title', 'price']


class Login(forms.Form):
    username = forms.CharField(max_length= 27)
    password = forms.CharField(max_length= 18)
