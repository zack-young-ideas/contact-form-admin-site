"""
Defines the form used to log in.
"""

from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        label='',
        min_length=1,
        max_length=64,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
