from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseName(models.Model):

    class Meta:
        abstract = True

    first_name = models.CharField(
        verbose_name=_('Имя'),
        max_length=256
    )

    last_name = models.CharField(
        verbose_name=_('Фамилия'),
        max_length=256
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
