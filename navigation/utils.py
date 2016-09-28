# -*- coding:utf-8 -*-
from django.conf.urls import *
from django.views.generic import TemplateView

from .models import Subdivision
from .context_processors import getNavigationProperties


def addUrl(template_flat_pages):
    sub = Subdivision.objects.filter(published=True)
    urlpatterns = []

    for s in sub:
        path = s.__url__()
        kwards = eval(s.kwards) if s.kwards else {}
        if path == '/':
            path = ''
        else:
            path += '/'
        if s.pageview:
            try:
                exec('from %s import urlpatterns as sub_urlpatterns' % s.pageview)
                urlpatterns.append(url(r'^%s' % path, include(s.pageview), kwargs=kwards))
            except ImportError:
                urlpatterns.append(url(r'^%s$' % path, s.pageview, kwargs=kwards))
        else:
            urlpatterns.append(url(r'^%s$' % path, TemplateView.as_view(template_name=template_flat_pages),
                                            kwargs=kwards))
    return urlpatterns


def branchAppend(request, param):
    """
    Add custom Subdivision in Branch
    """
    branch = getNavigationProperties(request)['NAVIGATION_BRANCH']

    if request.META['PATH_INFO'] in ['', '/']:
        return branch

    address = request.META['PATH_INFO'].split('/')[-1]
    sub = Subdivision(address=address, **param)
    branch.append(sub)
    return branch


