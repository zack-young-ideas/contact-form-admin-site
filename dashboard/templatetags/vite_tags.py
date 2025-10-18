from django import template

from dashboard.utils import get_vite_asset


register = template.Library()


@register.simple_tag
def vite_assets(path):
    """
    Usage:
        {% vite_asset 'assets/javascript/dashboard-modal/main.tsx' %}
    Returns the URL to the built JS file.
    """
    return get_vite_asset(path)
