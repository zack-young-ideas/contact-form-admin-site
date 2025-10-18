"""
Defines a decorator that returns 404 if the user is not authenticated.
"""

from functools import wraps
import json
import os

from django.conf import settings
from django.http import Http404


_manifest = None


def get_vite_asset(path: str) -> str:
    """
    Returns the path to the built asset from manifest.json.
    """
    global _manifest

    if settings.DEBUG:
        # In dev mode, retrieve files from Vite's dev server instead.
        return [f'http://localhost:5173/{path}']

    static_dir = os.path.join(settings.BASE_DIR, 'static')
    if settings.STATIC_ROOT:
        static_dir = settings.STATIC_ROOT

    if _manifest is None:
        manifest_path = os.path.join(
            static_dir,
            '.vite',
            'manifest.json'
        )
        with open(manifest_path, 'r') as f:
            _manifest = json.load(f)

    entry_data = _manifest.get(path)
    files = []

    if not entry_data:
        raise ValueError(f"Asset '{path}' not found in Vite manifest")

    for imp in entry_data.get('imports', []):
        files.append(settings.STATIC_URL + _manifest[imp]['file'])

    files.append(settings.STATIC_URL + entry_data['file'])
    return files


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
