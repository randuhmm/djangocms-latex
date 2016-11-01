# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import shutil
from subprocess import call
from tempfile import mkdtemp

from cms.models.pluginmodel import CMSPlugin
from django.core.files.images import ImageFile
from django.db import models


EQUATION_TEMPLATE = '''
\\documentclass[20pt]{article}
\\usepackage{graphicx}
\\begin{document}
\\pagestyle{empty}
\\begin{displaymath}
%s
\\end{displaymath}
\\end{document}
'''


def equation_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/equations/<id>/<filename>
    return 'equations/{0}/{1}'.format(instance.id, filename)


class LatexEquationPlugin(CMSPlugin):
    equation = models.TextField()
    image = models.ImageField(null=True, blank=False,
                              upload_to=equation_directory_path)

    _original_equation = None

    def __init__(self, *args, **kwargs):
        super(LatexEquationPlugin, self).__init__(*args, **kwargs)
        self._original_equation = self.equation

    def post_save(self, created):
        if self._original_equation != self.equation or created:
            self._original_equation = self.equation
            original_dir = os.getcwd()

            try:
                # Generate the png file
                out_dir = mkdtemp()
                os.chdir(out_dir)
                tex_file = os.path.join(out_dir, 'equation.tex')
                dvi_file = os.path.join(out_dir, 'equation.dvi')
                png_file = os.path.join(out_dir, 'equation1.png')
                with open(tex_file, 'w') as f:
                    f.write(EQUATION_TEMPLATE % self.equation)
                call(['latex', '-interaction', 'nonstopmode', '-halt-on-error',
                      '-file-line-error', tex_file])
                call(['dvipng', '-T', 'tight', '-D', '144', dvi_file])

                # Write the file
                with open(png_file, 'rb') as f:
                    image_file = ImageFile(f)
                    image_name = 'equation.png'
                    self.image.save(image_name, image_file)

                # Remove temporary files
                shutil.rmtree(out_dir)

            except Exception, e:
                print e

            os.chdir(original_dir)
