from django import forms
from inventory.models import Customer,Game,Assign
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username' , 'email' , 'password')        

class NewCustomerForm(forms.ModelForm):
    class Meta():
        app_label = 'inventory'
        model = Customer
        fields = '__all__'

class AssigningForm(forms.ModelForm):
    class Meta():
        app_label = 'inventory'
        model = Assign
        fields = '__all__'

class AddGameForm(forms.ModelForm):
    class Meta():
        app_label = 'inventory'
        model = Game
        fields = '__all__'
