
from django import forms
from django.forms import ModelForm
from users.models import UserInfo


class UpdateForm(ModelForm):
    pass


class user_UpdateForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"
        required_fields = ['username', 'email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': ' form-control mb-3 '}),
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'password': forms.TextInput(attrs={'class': 'form-control mb-3'})
        }
        labels = {
            'email': 'email',
            'username': 'Username',
            'password': 'Password'
        }