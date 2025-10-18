"""
Defines a DEBUG_IS_TRUE variable to check if DEBUG is set to True.
"""

from django.conf import settings


def global_variables(request):
    return {
        'DEBUG_IS_TRUE': settings.DEBUG,
    }
