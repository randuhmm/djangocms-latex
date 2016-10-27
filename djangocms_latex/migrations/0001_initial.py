# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_latex.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatexEquationPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_latex_latexequationplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('equation', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=djangocms_latex.models.equation_directory_path)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
