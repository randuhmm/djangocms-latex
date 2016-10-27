# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from . import models


class LatexEquationCMSPlugin(CMSPluginBase):
    model = models.LatexEquationPlugin
    name = _('Equation')
    module = _('Latex')
    # change_form_template = 'admin/djangocms_latex/equation.html'
    render_template = 'djangocms_latex/equation.html'
    text_enabled = True

    fieldsets = (
        (None, {'fields': (
            'equation',
        )}),
    )


plugin_pool.register_plugin(LatexEquationCMSPlugin)
