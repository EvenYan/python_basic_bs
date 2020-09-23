from django.db import models

# Create your models here.
class PeopleInfo(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=400)
