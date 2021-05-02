from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    email = forms.CharField(max_length=100, required=True, widget=forms.EmailInput())
    first_name=forms.CharField(max_length=50, required=True,help_text="Il tuo nome")
    last_name = forms.CharField(max_length=50, required=True, help_text="Il tuo cognome")
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        #fields = [ 'username', 'password1', 'password2']