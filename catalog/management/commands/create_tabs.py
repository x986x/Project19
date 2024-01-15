from django.core.management.base import BaseCommand
import json
from catalog import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Очистка базы данных от старых данных
        models.Category.objects.all().delete()

        with open('catalog/fixtures/category.json') as file:
            info_category = json.load(file)

        info_str = []
        for data in info_category:
            info_str.append(models.Category(**data["fields"]))

        # Добавление новых данных в базу данных
        models.Category.objects.bulk_create(info_str)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))