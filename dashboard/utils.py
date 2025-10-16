"""
Defines a decorator that returns 404 if the user is not authenticated.
"""

from functools import wraps

from django.http import Http404


def modified_login_required(view_function):
    """
    Decorator that returns 404 response if user is not authenticated.
    """
    @wraps(view_function)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_function(request, *args, **kwargs)
        else:
            raise Http404()
    return wrapper
