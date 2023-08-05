from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', min_length=2, max_length=15,widget= forms.TextInput
                           (attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='last_name', min_length=2, max_length=15,widget= forms.TextInput
                           (attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(label='email', widget= forms.EmailInput
                           (attrs={'placeholder':'Email'}))
    username = forms.CharField(label='username', min_length=8, max_length=15,widget= forms.TextInput
                           (attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='password1', min_length=8, max_length=15,widget= forms.PasswordInput
                           (attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='password2', min_length=8, max_length=15,widget= forms.PasswordInput
                           (attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[a-zA-Z]+$', first_name):
            raise forms.ValidationError("First name must only contain letters...")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[a-zA-Z]+$', last_name):
            raise forms.ValidationError("Last name must only contain letters...")
        return last_name

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError("Usernames must only contain letters and numbers...")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered to an account...")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if not re.match(r'^[a-zA-Z0-9]+$', password1):
            raise forms.ValidationError("Password must only contain letters and numbers...")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if not re.match(r'^[a-zA-Z0-9]+$', password2):
            raise forms.ValidationError("Password must only contain letters and numbers...")
        return password2
    

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not re.match(r'^[a-zA-Z]+$', first_name):
            raise forms.ValidationError("First name must only contain letters...")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not re.match(r'^[a-zA-Z]+$', last_name):
            raise forms.ValidationError("Last name must only contain letters...")
        return last_name

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError("Usernames must only contain letters and numbers...")
        return username