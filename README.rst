djangocms-latex
===============

.. image:: https://travis-ci.org/randuhmm/djangocms-latex.svg?branch=master
    :target: https://travis-ci.org/randuhmm/djangocms-latex
    :alt: Latest Travis CI build status

.. image:: https://coveralls.io/repos/github/randuhmm/djangocms-latex/badge.svg?branch=master
    :target: https://coveralls.io/github/randuhmm/djangocms-latex?branch=master
    :alt: Latest Coveralls test coverage

.. image:: https://readthedocs.org/projects/rad-esp8266/badge/?version=latest
    :target: http://rad-esp8266.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

LaTEX plugin for django CMS 3.0

Supported Python version:

* Python 2.7
* Python 3.3
* Python 3.4
* Python 3.5

Supported Django versions:

* Django 1.8
* Django 1.9
* Django 1.10

Supported django CMS versions:

* django CMS 3.x

Documentation
-------------

The full documentation is at http://djangocms-latex.rtfd.org.

Quickstart
----------

#. Install the ``latex`` and ``dvipng`` command-line programs.
   See `TeX Live <https://www.tug.org/texlive/>`_
   for detailed instructions for your OS.

   Ubuntu::

    sudo apt-get -qq update;
    sudo apt-get install -y texlive;
    sudo apt-get install -y dvipng;

#. Install djangocms-latex::

    pip install djangocms-latex

#. Add to INSTALLED_APPS::

    'djangocms_latex',

#. Update the database schema::

    $ python manage migrate djangocms_latex

#. Add "**latex equation**" plugin to your placeholders


