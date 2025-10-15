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


def dashboard(request):
    """
    The admin dashboard main page.
    """
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        raise Http404()
