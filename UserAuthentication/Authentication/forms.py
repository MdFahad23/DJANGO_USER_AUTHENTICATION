from  django import forms
from django.contrib.auth.models import User
from Authentication.models import UserInfo


class UserFrom(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserInfoFrom(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['facebook_id', 'profile_pic']

