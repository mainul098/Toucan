from django.contrib.auth.models import User
from django import forms

from twitter.models import Tweet


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class TweetFrom(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Tweet
        fields = ['content']
