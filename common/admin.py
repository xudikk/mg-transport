from django.contrib import admin
from . import models


class BaseModelAdmin(admin.ModelAdmin):
    list_per_page = 15


@admin.register(models.Region)
class RegionAdmin(BaseModelAdmin):
    list_display = ("id", "name", "soato")
    list_display_links = ("id", "name", "soato")
    search_fields = ("name", "soato")


@admin.register(models.District)
class DistrictAdmin(BaseModelAdmin):
    list_display = ("id", "name", "region", "soato")
    list_display_links = ("id", "name", "region", "soato")
    search_fields = (
        "name",
        "soato",
    )
    list_filter = ("region",)
    autocomplete_fields = ("region",)
