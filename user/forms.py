from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Passwords are not same')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That username is already taken. Please, choose another one.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This e-mail address is already registered in our website.")

        values = {

            'username': username,
            'password': password,
            'email': email,
        }

        return values


class LoginForm(forms.Form):
    username = forms.CharField(label='Username:')
    password = forms.CharField(label='Password: ', widget=forms.PasswordInput)


class ChangePassword(forms.Form):
    old_password = forms.CharField(label='Current password: ', widget=forms.PasswordInput)
    new_password = forms.CharField(label='New password:', widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label='Confirm new password:', widget=forms.PasswordInput)

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise forms.ValidationError('Passwords are not same')

        values = {
            'old_password': old_password,
            'new_password': new_password,
            'confirm_new_password': confirm_new_password,
        }

        return values


class ChangeUsername(forms.Form):
    new_username = forms.CharField(label='Username: ')

    def clean(self):
        new_username = self.cleaned_data.get('new_username')

        if User.objects.filter(username=new_username).exists():
            raise forms.ValidationError("That username is already taken.Please, choose another one")

        values = {
            'new_username': new_username,
        }

        return values
