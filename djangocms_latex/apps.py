from __future__ import unicode_literals

from django.apps import AppConfig


class DjangocmsLatexConfig(AppConfig):
    name = 'djangocms_latex'

    def ready(self):
        from djangocms_latex import signals  # noqa
