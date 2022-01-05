from django import forms
from . models import Signup

class SignupForm(forms.ModelForm):
    Password =forms.CharField(widget=forms.PasswordInput,max_length=8)
    Confirmpassword = forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields='__all__'
class LoginForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,max_length=8)
    class Meta():
        model=Signup
        fields=('Email','Password')
        
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Signup
        fields=('Name','Age','Place','Email','Photo')