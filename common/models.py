from django.db import models
from django.utils.translation import gettext_lazy as _
from base.db import TimeStampedModel


class Region(TimeStampedModel):
    name = models.CharField(verbose_name=_("Nomi"), max_length=255)
    soato = models.CharField(verbose_name=_("Soato"), max_length=50, unique=True)

    class Meta:
        db_table = "regions"
        verbose_name = _("Viloyat")
        verbose_name_plural = _("Viloyatlar")

    def __str__(self) -> str:
        return self.name


class District(TimeStampedModel):
    class Meta:
        db_table = "districts"
        verbose_name = _("Tuman")
        verbose_name_plural = _("Tumanlar")

    name = models.CharField(verbose_name=_("Nomi"), max_length=255)
    region = models.ForeignKey(
        verbose_name=_("Viloyat"),
        to="common.Region",
        on_delete=models.CASCADE,
        related_name="districts",
    )
    soato = models.CharField(verbose_name=_("Soato"), max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
