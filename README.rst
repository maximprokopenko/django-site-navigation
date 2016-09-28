Navigation on the site using flat pages, URL patterns and Views
===============================================================

-  install using pip:

.. code:: bash

        pip install django-site-navigation

-  add "site\_navigation" to your INSTALLED\_APPS:

.. code:: python

    INSTALLED_APPS = (
        ...
        'site_navigation'
    )

-  add "site\_navigation.context\_processors.getNavigationProperties" to
   your TEMPLATE\_CONTEXT\_PROCESSORS:

.. code:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'site_navigation.context_processors.getNavigationProperties'
    )

-  add "site\_navigation.middleware.RedirectMiddleware" to your
   MIDDLEWARE\_CLASSES:

.. code:: python

    MIDDLEWARE_CLASSES = (
        ...
        'site_navigation.middleware.RedirectMiddleware'
    )

-  add in urls.py:

.. code:: python

    from navigation.utils import addUrl
    urlpatterns += addUrl('default_page.html')

-  create table:

.. code:: bash

        python ./manage.py migrate

-  create templates:
   default\_page.html

.. code:: html


        {% load site-navigation %}
        <!DOCTYPE html>
        <html>
        <head lang="en">
            <meta charset="UTF-8">
            <meta name="description" content="{{ NAVIGATION_SUBDIVISION.description|default_if_none:'' }}">
            <meta name="keywords" content="{{ NAVIGATION_SUBDIVISION.keywords|default_if_none:'' }}">
            <title>
                <title>
                    {% if NAVIGATION_SUBDIVISION.title %}{{ NAVIGATION_SUBDIVISION.title }}
                    {% elif NAVIGATION_SUBDIVISION.pageTitle %} {{ NAVIGATION_SUBDIVISION.pageTitle }}
                    {% elif NAVIGATION_SUBDIVISION.name %}{{ NAVIGATION_SUBDIVISION.name }}
                    {% else %}{{ SITE_OPTIONS.title }}{% endif %}
                </title>
            </title>
        </head>
        <body>
        
        {% breadcrumbs %}
        
        <h1>
            {% if NAVIGATION_SUBDIVISION.pageTitle %}
                {{ NAVIGATION_SUBDIVISION.pageTitle }}
            {% else %}
                {{ NAVIGATION_SUBDIVISION.name }}
            {% endif %}
        </h1>
        
        
        {% block beforecontent %}
            {{ NAVIGATION_SUBDIVISION.before|default_if_none:''|safe }}
        {% endblock %}
        
        {% block content %}{% endblock %}
        
        {% block aftercontent %}
            {{ NAVIGATION_SUBDIVISION.after|default_if_none:''|safe }}
        {% endblock %}
        
        </body>
        </html>

menu.html

.. code:: html


        {% for sub in subdivisions|dictsortreversed:"priority" %}
            <li {% if sub == NAVIGATION_SUBDIVISION %} class="active" {% endif %}>
                <a href="{{ sub.getUrl }}" >
                    {{ sub }}
                </a>
            </li>
        {% endfor %}

breadcrumbs.html

.. code:: html


        <ul>
            <li><a href="/">Home</a></li>
            {% for s in NAVIGATION_BRANCH %}
                <li>{% if not forloop.last %}
                        <a href="{{ s.getUrl }}">{{ s.name }}</a>
                     {% else %}
                        {{ s.name }}
                     {% endif %}
                </li>
            {% endfor %}
        </ul>

