from django.db import models
from datetime import datetime

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    giver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='giver')
    receiver = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='receiver')
    year = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return f"{self.giver.name} -> {self.receiver.name}"