===============
django-sb-admin
===============

Introduction
------------

Django SB Admin is a Django app which provides a Bootstrap 3 Dashboard theme:

http://startbootstrap.com/template-overviews/sb-admin/

SB Admin is a free to download Bootstrap admin template. This template uses the
default Bootstrap 3 styles along with a variety of powerful jQuery plugins to 
create a pwerful framework for creating admin panels, web apps, or back-end dashboards.

Installation
------------

1. Install an app

   pip install https://github.com/bluszcz/django-sb-admin.git

2. Add "django_smb_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_smb_app',
    )

3. Extend a base template:

   {% extends "django_sb_admin/base.html" %}

License
-------

Copyright 2015 Rafał Zawadzki

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