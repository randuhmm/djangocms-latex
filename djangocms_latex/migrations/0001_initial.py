# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import djangocms_latex.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatexEquationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(
                    parent_link=True, related_name='djangocms_latex_latexequat'
                    'ionplugin', auto_created=True, primary_key=True,
                    serialize=False, to='cms.CMSPlugin')),
                ('equation', models.TextField()),
                ('image', models.ImageField(
                    null=True,
                    upload_to=djangocms_latex.models.equation_directory_path)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
