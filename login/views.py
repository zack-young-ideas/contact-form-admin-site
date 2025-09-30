from django.shortcuts import render

from login import forms


def login_page(request):
    """
    The public login page for the admin site.
    """
    context = {'form': forms.LoginForm()}
    return render(request, 'login/login_page.html', context)
