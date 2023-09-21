from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from base.db import TimeStampedModel


class Department(TimeStampedModel):
    class Meta:
        db_table = 'department'
        verbose_name = _("Bo'linma")
        verbose_name_plural = _("Bo'linmalar")

    class TypeChoices(models.TextChoices):
        GUARDING = 'guarding', _("Qo'riqlash bo'linma")
        MILITARY = 'military', _("Harbiy bo'linma")

    name = models.CharField(max_length=255, verbose_name=_('Nomi'))
    type = models.CharField(max_length=100, verbose_name=_('Turi'), choices=TypeChoices.choices, )
    district = models.ForeignKey(
        to='common.District', on_delete=models.CASCADE, verbose_name=_('Tuman'), related_name='departments'
    )
    legal_address = models.CharField(
        max_length=255,
        verbose_name=_("Yuridik manzili"),
        null=True,
        blank=True,
    )
    stir = models.CharField(max_length=9, verbose_name=_('STIR'), null=True, blank=True)

    phone = PhoneNumberField(verbose_name=_("Telefon raqami"), null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

