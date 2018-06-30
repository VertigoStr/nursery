from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

from core.common import BaseName


class Parent(BaseName):

    class Meta:
        verbose_name = _('Родитель')
        verbose_name_plural = _('Родители')


class Child(BaseName):
    GENDER = Choices(
        (1, 'MALE', _('Мужской')),
        (2, 'FEMALE', _('Женский'))
    )

    class Meta:
        verbose_name = _('Ребенок')
        verbose_name_plural = _('Дети')

    gender = models.PositiveSmallIntegerField(
        verbose_name=_('Пол'),
        choices=GENDER,
        default=GENDER.MALE
    )

    grade = models.PositiveSmallIntegerField(
        verbose_name=_('Класс'),
        default=1
    )

    photo = models.ImageField(
        verbose_name=_('Фото')
    )

    is_studying = models.BooleanField(
        verbose_name=_('Учится'),
        default=False
    )

    parents = models.ManyToManyField(
        to=Parent,
        blank=True
    )

    date_of_birth = models.DateField(
        verbose_name=_('Дата рождения')
    )
