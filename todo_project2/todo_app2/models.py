import datetime

from django.db import models

# Create your models here.
class Todoapp(models.Model):
    name=models.CharField(max_length=20)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today)