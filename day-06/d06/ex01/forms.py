from django.forms import ModelForm, TextInput, PasswordInput
from .models import signUp, logIn
class signUpForm(ModelForm):
    
    class Meta:
        model = signUp
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'}),
            'confirm_password': PasswordInput(attrs={'placeholder': 'confirm_password'}),
        }

class logInForm(ModelForm):
    
    class Meta:
        model = logIn
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'password': PasswordInput(attrs={'placeholder': 'password'}),
        }