===============
django-sb-admin
===============

.. image:: https://devcarpet.net/images/github/b3d2cfe66830794ce35bdee04bbe74f6.jpg

Introduction
------------

Django SB Admin is a resuable Django app which provides a Bootstrap 3 SB Admin dashboard theme:

http://startbootstrap.com/template-overviews/sb-admin/

SB Admin is a free to download Bootstrap admin template. This template uses the
default Bootstrap 3 styles along with a variety of powerful jQuery plugins to 
create a powerful framework for creating admin panels, web apps, or back-end dashboards.

Installation
------------

1. Install an app::

    pip install django-sb-admin

2. Add "django_sb_admin" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_sb_admin',
    )

3. If you want to see an example app, add following to your urls file::

    url(r'^django-sb-admin/', include('django_sb_admin.urls')),

Usage
-----

.. image:: https://devcarpet.net/images/github/c0b56b47dd7f199073fbca887b79a6f5.jpg

1. Copy following blank template::

    django_sb_admin/sb_admin_blank.html

or:

2. Extend a base template::

    {% extends "django_sb_admin/base.html" %}

and then:

3. Override following blocks::

    {% block sb_admin_header %}<!-- Header of the page -->{% endblock sb_admin_header %}
    {% block sb_admin_title %}<!-- Title of the content the page -->{% endblock sb_admin_title %}
    {% block sb_admin_sidebar %}<!-- left sidebar -->{% endblock sb_admin_sidebar %}
    {% block sb_admin_navbar_right %}<!-- right top navbar -->{% endblock sb_admin_navbar_right %}
    {% block sb_admin_content %}<!-- content -->{% endblock sb_admin_content %}

To use included login page put following in your **urls.py**::

    url(r'^accounts/login/$', auth_views.login, 
        {'template_name': 'django_sb_admin/examples/login.html'}),


Conventions
-----------

Template blocks
===============

* Names  of blocks start with *sb_admin* 

Extras
------

* login template
* messages support in a base template

License
-------

Copyright 2015 Rafal Zawadzki

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

SB Admin itself is licensed under the Apache License 
https://github.com/IronSummitMedia/startbootstrap-sb-admin/blob/gh-pages/LICENSE
