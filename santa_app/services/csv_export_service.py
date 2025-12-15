import csv
import os
from django.conf import settings
from santa_app.models import Assignment
from datetime import datetime


class CSVExportService:
    @staticmethod
    def export(year=None):
        if not year:
            year = datetime.now().year

        filename = f'secret_santa_{year}.csv'
        output_path = os.path.join(settings.MEDIA_ROOT, filename)

        assignments = Assignment.objects.filter(year=year)

        with open(output_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Employee_Name",
                "Employee_EmailID",
                "Secret_Child_Name",
                "Secret_Child_EmailID"
            ])

            for a in assignments:
                writer.writerow([
                    a.giver.name,
                    a.giver.email,
                    a.receiver.name,
                    a.receiver.email
                ])

        return settings.MEDIA_URL + filename
