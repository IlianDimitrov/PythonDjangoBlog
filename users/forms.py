from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #c = [("1", "Male"),("2", "Female")]
    email = forms.EmailField()
    #gender = forms.ChoiceField(choices=c, label="Gender")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #'gender']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
