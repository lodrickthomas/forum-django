from django.conf import settings
from django.shortcuts import redirect
import re
from django.contrib.auth import logout
from django.urls import reverse



EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class loginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request,'user')
        path = request.path_info.lstrip('/')

        # if not request.user.is_authenticated:
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)

        url_is_exempted = any(url.match(path) for url in EXEMPT_URLS)

        if path == reverse('logout').lstrip('/'):
            logout(request)

        # dont use request.user.is_authenticated() appended with brackets
        if request.user.is_authenticated and not url_is_exempted:
            return redirect(settings.LOGIN_URL)

        elif request.user.is_authenticated or url_is_exempted:
            return None

        else:
            return redirect(settings.LOGIN_URL)
