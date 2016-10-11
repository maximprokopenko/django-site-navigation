# -*- coding:utf-8 -*-
from django.conf.urls import *
from django.views.generic import TemplateView

from .models import Subdivision
from .context_processors import get_navigation_properties


def navigation_urls(template_flat_pages):
    """
    Get navigation Urls
    """
    sub = Subdivision.objects.filter(published=True)
    urlpatterns = []

    for s in sub:
        path = s.__url__()
        kwargs = eval(s.kwargs) if s.kwargs else {}
        if path == '/':
            path = ''
        else:
            path += '/'
        if s.pageView:
            try:
                exec('from %s import urlpatterns as sub_urlpatterns' % s.pageView)
                urlpatterns.append(url(r'^%s' % path, include(s.pageView), kwargs=kwargs))
            except ImportError:
                urlpatterns.append(url(r'^%s$' % path, s.pageView, kwargs=kwargs))
        else:
            urlpatterns.append(url(r'^%s$' % path, TemplateView.as_view(template_name=template_flat_pages),
                                   kwargs=kwargs))
    return urlpatterns


def branch_append(request, param):
    """
    Add custom Subdivision in Branch.
    If dict param not include key 'address', property 'address' will be taken from request
    """
    branch = get_navigation_properties(request)['NAVIGATION_BRANCH']

    if 'address' not in param:
        if request.META['PATH_INFO'] in ['', '/']:
            return branch

        address = request.META['PATH_INFO'].split('/')[-1]
        sub = Subdivision(address=address, **param)
    else:
        sub = Subdivision(**param)

    branch.append(sub)
    return branch


