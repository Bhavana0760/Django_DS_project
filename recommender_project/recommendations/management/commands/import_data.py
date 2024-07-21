# recommendations/management/commands/import_data.py
from django.core.management.base import BaseCommand
import pandas as pd
from recommendations.models import Tshirt

class Command(BaseCommand):
    help = 'Imports data from dataset.xlsx into the Tshirt model'

    def handle(self, *args, **kwargs):
        file_path = "recommender_project\dataset.xlsx"
        df = pd.read_excel(file_path)

        for index, row in df.iterrows():
            Tshirt.objects.create(
                product_id=row['product_id'],
                height=row['height'],
                weight=row['weight'],
                color_of_tshirt=row['color_of_tshirt'],
                size_of_tshirt=row['size_of_tshirt'],
                price=row['price']
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
