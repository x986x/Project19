from django.core.management import BaseCommand, call_command
from django.db import IntegrityError
import os
from django.conf import settings
from catalog import models

from catalog.models import Product

class Command(BaseCommand):
    help = 'Load data from fixtures into the database'

    def handle(self, *args, **options):
        models.Category.objects.all().delete()
        category_fixture_path = os.path.join(settings.BASE_DIR, 'catalog', 'fixtures', 'category.json')
        product_fixture_path = os.path.join(settings.BASE_DIR, 'catalog', 'fixtures', 'products.json')

        try:
            call_command('loaddata', category_fixture_path)
            call_command('loaddata', product_fixture_path)
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Invalid fixtures: {e}'))
        else:
            self.stdout.write(self.style.SUCCESS('OK'))
