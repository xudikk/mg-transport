from rest_framework import serializers

from . import models


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = [
            "id",
            "name",
            "soato",
        ]


class DistrictSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = models.District
        fields = [
            "id",
            "name",
            "region",
            "soato",
        ]
