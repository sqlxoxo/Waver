# core/forms.py

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput)
   password_confirm = forms.CharField(widget=forms.PasswordInput)

   class Meta:
      model = User
      fields = ['username', 'email', 'password']

   def clean(self):
      cleaned_data = super().clean()
      password = cleaned_data.get("password")
      password_confirm = cleaned_data.get("password_confirm")
      
      if password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")

class UserLoginForm(forms.Form):
   username = forms.CharField(max_length=150)
   password = forms.CharField(widget=forms.PasswordInput)
