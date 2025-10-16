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
                'placeholder': 'Password'
            }
        )
    )


class TwoFactorAuthForm(forms.Form):

    factor = forms.ChoiceField(
        choices=[
            ('phone', 'Phone'),
            ('email', 'Email'),
        ],
        widget=forms.RadioSelect,
        label='Select a factor'
    )
    phone = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'
            }
        )
    )
    email = forms.EmailField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }
        )
    )
