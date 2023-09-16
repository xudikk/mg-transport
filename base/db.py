from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Yaratilgan vaqti"), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("O'zgartirilgan vaqti"), auto_now=True
    )

    class Meta:
        abstract = True


class GenderChoices(models.TextChoices):
    MALE = "male", _("Erkak")
    FEMALE = "female", _("Ayol")
