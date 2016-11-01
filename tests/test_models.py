# -*- coding: utf-8 -*-
"""
test_djangocms_latex
------------

Tests for `djangocms_latex` modules module.
"""
from __future__ import absolute_import, print_function, unicode_literals

from cms.views import details
from django.contrib.auth.models import AnonymousUser
from djangocms_latex.models import LatexEquationPlugin

from . import BaseTest


class TestLatexModels(BaseTest):

    example_equation = r'x=\\frac{a}{b}'

    def test_add_plugin(self):
        from cms.api import add_plugin
        page_1, page_2 = self.get_pages()
        data = {
            'equation': self.example_equation,
        }
        placeholder = page_1.placeholders.get(slot='content')
        add_plugin(placeholder, 'LatexEquationCMSPlugin', 'en', **data)
        page_1.publish('en')

        # Get published page
        public = page_1.get_public_object()
        # plugin is the plugin instance we're going to render
        plugin = public.placeholders.get(slot='content').get_plugins_list()[0]

        request = self.get_page_request(public, AnonymousUser())
        response = details(request, '')

        self.assertContains(response, '<img class="responsive" src="/media/'
                            'equations/%s/equation.png" />' % plugin.pk)

    def test_model_save(self):

        plugin = LatexEquationPlugin()
        plugin.equation = self.example_equation
        plugin.save()

        self.assertEqual(self.example_equation, plugin.equation)
