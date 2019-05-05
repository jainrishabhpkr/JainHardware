from django import forms
from django.contrib.auth.models import User

class GuestForm(forms.Form):
    email = forms.EmailField()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"your full name"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"your content"}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        print('email validation')
        print(email)
        if  email[len(email)-9:]!="gmail.com":
            print("apple")
            raise forms.ValidationError("must be gmail")
        name = cleaned_data.get('fullname')
        print("name validation")
        print(name)
        if len(name)<6:
            raise forms.ValidationError(" must be more than 6 ")




class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm passsword',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username =cleaned_data.get('username')
        qs1 = User.objects.filter(username=username)
        if qs1.exists():
            raise forms.ValidationError("username is taken")
        email =cleaned_data['email']
        qs2 = User.objects.filter(email=email)
        if qs2.exists():
            raise forms.ValidationError("email already exists")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("password must match")
