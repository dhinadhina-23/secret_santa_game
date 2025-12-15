import csv
import os
import random
from datetime import datetime
from django.conf import settings
from santa_app.models import Employee, Assignment


class SecretSantaManager:
    def __init__(self, csv_file_path, previous_pairs=None):
        self.csv_file_path = csv_file_path
        self.previous_pairs = previous_pairs or {}
        self.employees = []
        self.assignments = {}

    # 1️⃣ Load employees from uploaded CSV
    def load_employees(self):
        with open(self.csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp, _ = Employee.objects.get_or_create(
                    name=row['Employee_Name'],
                    email=row['Employee_EmailID']
                )
                self.employees.append(emp)

    # 2️⃣ Generate Secret Santa assignments (no self / no previous repeat)
    def generate_assignments(self):
        if len(self.employees) < 2:
            raise ValueError("Not enough employees")

        givers = self.employees[:]
        receivers = self.employees[:]

        for _ in range(1000):
            random.shuffle(receivers)
            temp = {}
            valid = True

            for g, r in zip(givers, receivers):
                if g.email == r.email:
                    valid = False
                    break
                if self.previous_pairs.get(g.email) == r.email:
                    valid = False
                    break
                temp[g] = r

            if valid:
                self.assignments = temp
                self._save_to_db()
                return temp

        raise ValueError("Valid assignment not possible")

    # 3️⃣ Save assignments to DB with year
    def _save_to_db(self):
        year = datetime.now().year
        Assignment.objects.filter(year=year).delete()

        for giver, receiver in self.assignments.items():
            Assignment.objects.create(
                giver=giver,
                receiver=receiver,
                year=year
            )

    # 4️⃣ EXPORT RESULT TO CSV  ✅ (THIS WAS MISSING)
    def export_to_csv(self):
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        filename = f"secret_santa_{datetime.now().year}.csv"
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                "Employee_Name",
                "Employee_EmailID",
                "Secret_Child_Name",
                "Secret_Child_EmailID"
            ])

            for giver, receiver in self.assignments.items():
                writer.writerow([
                    giver.name,
                    giver.email,
                    receiver.name,
                    receiver.email
                ])

        return settings.MEDIA_URL + filename
