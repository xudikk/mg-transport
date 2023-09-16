import json
import tqdm

from django.db import transaction
from django.core.management.base import BaseCommand

from common.models import Region, District


class Command(BaseCommand):
    help = "Load regions and districts"

    def handle(self, *args, **options):
        with open("common/management/data/regions.json", "r", encoding="utf-8") as f:
            regions_json_data = json.load(f)
        with open("common/management/data/districts.json", "r", encoding="utf-8") as f:
            districts_json_data = json.load(f)

        for region in tqdm.tqdm(regions_json_data):
            with transaction.atomic():
                n_region, created = Region.objects.update_or_create(
                    id=region["id"],
                    defaults={"name": region["name_uz"], "soato": region["soato"]},
                )

        for district in tqdm.tqdm(districts_json_data):
            with transaction.atomic():
                n_district, created = District.objects.update_or_create(
                    id=district["id"],
                    defaults={
                        "name": district["name_uz"],
                        "region": Region.objects.get(soato=str(district["soato"])[:4]),
                        "soato": district["soato"],
                    },
                )

        # write success
        self.stdout.write("Successfully loaded regions and districts!")
