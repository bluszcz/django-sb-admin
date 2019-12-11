# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sb-admin',
    version='5.5.1',
    packages=['django_sb_admin'],
    include_package_data=True,
    license='Apache License version 2.0',
    description='SB Admin dashboard bootstrap 4 theme packaged as a reusable Django app.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/bluszcz/django-sb-admin',
    author='Rafal Zawadzki',
    author_email='bluszcz@bluszcz.net',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
