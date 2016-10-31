#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1'

setup(
    name='djangocms-latex',
    version=version,
    description='Plugin for DjangoCMS 3.0 to include latex documents and'
                'equations in your content.',
    author='Jonny Morrill',
    author_email='jrmorrill@gmail.com',
    url='',
    packages=[
        str('djangocms_latex'),
    ],
    include_package_data=True,
    install_requires=[
        'django-cms>=3.0',
    ],
    test_suite='cms_helper.run',
)
