from django.db.models.signals import post_save
from django.dispatch import receiver
from djangocms_latex.models import LatexEquationPlugin


@receiver(post_save, sender=LatexEquationPlugin)
def latex_equation_post_save(sender, instance, created, *args, **kwargs):
    instance.post_save(created)
