# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from .models import Redirect


class RedirectMiddleware(object):
    def process_request(self, request):
        try:
            redirect = Redirect.objects.get(url_from=request.path)
            return HttpResponseRedirect(redirect.url_to)
        except Redirect.DoesNotExist:
            return None