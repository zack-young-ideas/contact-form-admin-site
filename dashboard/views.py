from django.contrib import auth
from django.shortcuts import redirect, render

from dashboard import forms, utils


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


@utils.modified_login_required
def logout_handler(request):
    """
    Logs a user out of the admin site.
    """
    auth.logout(request)
    return redirect('login')


@utils.modified_login_required
def dashboard(request):
    """
    The admin dashboard main page.
    """
    return render(request, 'dashboard/dashboard.html')
