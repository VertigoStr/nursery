from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from apps.child.models import Child, Parent


class Journal(models.Model):
    ACTION = Choices(
        (1, 'BRING', _('Привели')),
        (2, 'TAKE', _('Забрали'))
    )

    class Meta:
        verbose_name = _('Журнал')
        verbose_name_plural = _('Журналы')

    child = models.ForeignKey(
        to=Child,
        verbose_name=_('Ребенок'),
        on_delete=models.CASCADE
    )

    time = models.TimeField(
        verbose_name=_('Время')
    )

    action = models.PositiveSmallIntegerField(
        verbose_name=_('Событие'),
        choices=ACTION,
        default=ACTION.BRING
    )

    parent = models.ForeignKey(
        to=Parent,
        verbose_name=_('Родитель'),
        on_delete=models.CASCADE
    )

    date = models.DateField(
        verbose_name=_('Дата')
    )
