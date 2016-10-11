from django import template
from django.template.loader import get_template
from django.template import Context
from django.template import TemplateDoesNotExist

from ..models import Subdivision

register = template.Library()

@register.simple_tag(takes_context=True)
def menu(context, template='menu.html', filter=None):
    subs = None
    if not filter:
        filter = 'published=True, parent__isnull=True, show=True'
    exec('subs = Subdivision.objects.filter(%s)' % filter)
    try:
        t = get_template(template)
    except TemplateDoesNotExist:
        return "ERROR: not found template '%s' for navigations tag 'menu'" % (template,)
    return t.render(Context({'subdivisions': subs,
                             'context': context,
                             'NAVIGATION_SUBDIVISION': context.get('NAVIGATION_SUBDIVISION'),
                             'NAVIGATION_BRANCH': context.get('NAVIGATION_BRANCH')}))

@register.simple_tag(takes_context=True)
def breadcrumbs(context, template='breadcrumbs.html'):
    try:
        t = get_template(template)
    except TemplateDoesNotExist:
        return "ERROR: not found template '%s' for navigations tag 'breadcrumbs'" % (template,)
    return t.render(Context({'context': context,
                             'NAVIGATION_SUBDIVISION': context.get('NAVIGATION_SUBDIVISION'),
                             'NAVIGATION_BRANCH': context.get('NAVIGATION_BRANCH')}))

