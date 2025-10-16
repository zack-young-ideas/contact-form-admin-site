from django.contrib import auth
from django.http import Http404
from django.shortcuts import redirect, render

from login import forms


def login_page(request):
    """
    The public login page for the admin site.
    """
    context = {
        'form': forms.LoginForm(),
        'error': False,
    }
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
        context['error'] = True
    return render(request, 'login/login_page.html', context)


def logout_handler(request):
    """
    Logs a user out of the admin site.
    """
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')
    else:
        raise Http404()


def dashboard(request):
    """
    The admin dashboard main page.
    """
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        raise Http404()
