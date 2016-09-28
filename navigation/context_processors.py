# -*- coding:utf-8 -*-
from .models import Subdivision


def reversePath(request, path, branch):
    '''
    Функция возвращает объект Subdivision по url с учетом вложенности
    '''
    try:
        if len(path):
            address = path.pop(0)
        else:
            address = ''
        sub = Subdivision.objects.get(address=address, parent=branch[-1] if len(branch) else None)
        branch.append(sub)
    except Subdivision.DoesNotExist:
        # ситуация когда на каком-то шаге не нашли Subdivision
        return branch

    if len(branch) and not len(path):
        return branch

    if sub and len(path):
        return reversePath(request, path, branch)


def getNavigationProperties(request):
    """
    Добавляет в контекст свойства раздела
    """
    if request.META['PATH_INFO'] in ['', '/']:
        pathAsList = ['/', ]
    else:
        pathAsList = [p for p in request.META['PATH_INFO'].split('/') if p]
    branch = reversePath(request, pathAsList, [])

    if len(branch):
        return {
            'NAVIGATION_BRANCH': branch,
            'NAVIGATION_SUBDIVISION': branch[-1],
        }
    else:
        return {}