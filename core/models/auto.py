from django.db import models
from django.utils.translation import gettext_lazy as _

from base.db import TimeStampedModel, GenderChoices

from core.models import User


class AutoMotoTransportColor(TimeStampedModel):
    class Meta:
        db_table = 'auto_moto_transport_color'
        verbose_name = _('Avtomototransport rangi')
        verbose_name_plural = _('Avtomototransport ranglari')

    name = models.CharField(max_length=50, verbose_name=_('Nomi'))
    hex_code = models.CharField(max_length=7, verbose_name=_('Hex kodi'))

    def __str__(self):
        return self.name


class AutoTypeChoices(models.TextChoices):
    LIGHT_CAR = 'light_car', _("Yengil avtomobil")
    BUS = 'bus', _("Avtobus")
    MICROBUS = 'microbus', _("Mikroavtobus")
    TRAILER = 'trailer', _("Tirkama")
    SEMI_TRAILER = 'semi_trailer', _("Yarim tirkama")
    FREIGHT_CARRIER = 'freight_carrier', _("Yuk tashuvchi")
    FREIGHT_PASSENGER_CARRIER = 'freight_passenger_carrier', _("Yuk-yo'lovchi tashuvchi")
    SPECIAL = 'special', _("Maxsus")
    ELECTRONAKLIYOT = 'electronakliyot', _("Elektronakliyot")
    MOTONAKLIYOT = 'motonakliyot', _("Motonakliyot")
    OTHER = 'other', _("Boshqa")


class AutoBrand(TimeStampedModel):
    class Meta:
        db_table = 'auto_brand'
        verbose_name = _('Avtomobil markasi')
        verbose_name_plural = _('Avtomobil markalari')

    name = models.CharField(max_length=255, verbose_name=_('Nomi'))

    def __str__(self):
        return self.name


class AutoMotoTransportModel(TimeStampedModel):
    """ Avto rusumi. """
    brand = models.ForeignKey(
        to='AutoBrand', on_delete=models.CASCADE, verbose_name=_('Markasi'), related_name='models'
    )
    type = models.CharField(max_length=50, verbose_name=_('Turi'), choices=AutoTypeChoices.choices)
    name = models.CharField(max_length=255, verbose_name=_('Nomlanishi'))
    stay_place_count = models.PositiveSmallIntegerField(verbose_name=_("Turadigan joylar soni"), null=True, blank=True)
    seat_count = models.PositiveSmallIntegerField(
        verbose_name=_("O'rindiqlar(haydovchi bilan) soni"), null=True, blank=True
    )
    engine_power = models.DecimalField(
        verbose_name=_("Dvigatel quvvati"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    unladen_mass = models.DecimalField(
        verbose_name=_("Yuksiz og'irligi"),
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Kg")
    )
    full_mass = models.DecimalField(
        verbose_name=_("To'la og'irligi"),
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=_("Kg")
    )

    def __str__(self):
        return f"{self.brand.name} - {self.name}"


class AutoMotoTransport(TimeStampedModel):
    class Meta:
        db_table = 'auto_moto_transport'
        verbose_name = _('Avtomototransport')
        verbose_name_plural = _('Avtomototransportlar')

    class ManufactureAreaTypeChoices(models.TextChoices):
        UZBEKISTAN = 'uzbekistan', _("O'zbekistonda ishlab chiqarilgan")
        MDH = 'mdh', _("MDH da ishlab chiqarilgan")
        FOREIGN = 'foreign', _("Xorijiy mamlakatda ishlab chiqarilgan")

    class FuelTypeChoices(models.TextChoices):
        ELECTRICITY = 'electricity', _("Elektr")
        PETROL = 'petrol', _("Benzin")
        SPG_SNG_PETROL = 'spg_sng_petrol', _("SPG+SNG benzini")
        GBASNG = 'gbasng', _("GBASNG")
        GBASPG = 'gbaspg', _("GBASPG")
        DIESEL = 'diesel', _("Dizel")
        HYBRID = 'hybrid', _("Hibrid")

    department = models.ForeignKey(
        to="Department",
        verbose_name=_('Bo\'linma'),
        on_delete=models.CASCADE,
        related_name='auto_moto_transports',
        null=True,
    )

    manufactured_area = models.CharField(
        verbose_name=_('Ishlab chiqarilgan joyi'), max_length=50, choices=ManufactureAreaTypeChoices.choices
    )
    state_number = models.CharField(verbose_name=_('Davlat raqami'), max_length=50, unique=True)
    manufactured_year = models.PositiveSmallIntegerField(verbose_name=_('Ishlab chiqarilgan yili'))
    color = models.ForeignKey(
        to='AutoMotoTransportColor',
        on_delete=models.CASCADE,
        verbose_name=_('Rangi'),
        related_name='auto_moto_transports'
    )
    type = models.CharField(max_length=50, verbose_name=_('Avtomobil turi'), choices=AutoTypeChoices.choices)
    fuel_type = models.CharField(max_length=50, verbose_name=_("Yoqilg'i turi"), choices=FuelTypeChoices.choices)
    car_model = models.ForeignKey(
        to='AutoMotoTransportModel',
        on_delete=models.CASCADE,
        verbose_name=_('Rusumi'),
        related_name='auto_moto_transports'
    )
    engine_number = models.CharField(verbose_name=_('Dvigatel raqami'), max_length=50)
    kuzov_number = models.CharField(verbose_name=_('Kuzov raqami'), max_length=50)
    tex_talon_number = models.CharField(verbose_name=_('Tex. talon raqami'), max_length=50)
    shassi_number = models.CharField(verbose_name=_('Shassi raqami'), max_length=50)

    def __str__(self):
        return f"{self.type} - {self.car_model.name} - {self.state_number}"
