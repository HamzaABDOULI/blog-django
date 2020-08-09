from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text='Username may only contain alphanumeric characters or single hyphens, and cannot begin or end with a hyphen.')
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label='Passwod', help_text='Make sure it is at least 15 characters OR at least 8 characters including a number and a lowercase letter.'
    , widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(), min_length=8)
 
    class Meta:
        model = User 
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Confirm the same password')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('There is a registered user with this name')
        return cd['username']    

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')

class UserUpdateForm(forms.ModelForm):
    class Meta:
      
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        model = User
        fields = ('first_name','last_name','email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)        


