from cProfile import label
from django import forms
from home.models import Profile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class AlterProfileInformationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["City","FirstName","LastName","Email","Picture"]
        Widgets={
            'City':forms.Select(attrs={'class':'form-control'}),
            'FirstName':forms.TextInput(attrs={'class':'form-control','label':'First Name'}),
            'LastName':forms.TextInput(attrs={'class':'form-control','label':'Last Name'}),
            'Email':forms.EmailInput(attrs={'class':'form-control','label':'email'}),
            'Picture':forms.FileInput(attrs={'class':'form-control'}),
        }

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirmation=forms.CharField(widget=forms.PasswordInput, label='Password Confirmation')
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']
        def clean_password_confirmation(self):
            password=self.cleaned_data.get('password')
            password2=self.cleaned_data.get('password_confirmation')
            if password !=password2:
                raise forms.ValidationError("confirmation passwork do not match")
            return password2




class LoginForm(forms.Form):
    username =forms.CharField(
        widget=forms.TextInput(
        attrs={'class':'form-controle'}),
        label='username'
        )
    password =forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class':'form-controle'}),
        label='password'
        )

