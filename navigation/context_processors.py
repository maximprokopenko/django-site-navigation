# -*- coding:utf-8 -*-
from .models import Subdivision


def reverse_path(request, path, branch):
    '''
    The function finds Subdivision from url
    '''
    try:
        if len(path):
            address = path.pop(0)
        else:
            address = ''
        sub = Subdivision.objects.get(address=address, parent=branch[-1] if len(branch) else None)
        branch.append(sub)
    except Subdivision.DoesNotExist:
        # if Subdivision no found
        return branch

    if len(branch) and not len(path):
        return branch

    if sub and len(path):
        return reverse_path(request, path, branch)


def get_navigation_properties(request):
    """
    Add to context subdivisions properties
    """
    if request.META['PATH_INFO'] in ['', '/']:
        pathAsList = ['/', ]
    else:
        pathAsList = [p for p in request.META['PATH_INFO'].split('/') if p]
    branch = reverse_path(request, pathAsList, [])

    if len(branch):
        return {
            'NAVIGATION_BRANCH': branch,
            'NAVIGATION_SUBDIVISION': branch[-1],
        }
    else:
        return {}