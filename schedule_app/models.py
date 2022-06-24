from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from tour import settings


class Adddate(models.Model):
    during = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        # db_table = 'schedule_app_adddate'


class Hotplace(models.Model):
    tour = models.ForeignKey(Adddate, on_delete=models.CASCADE, null=True)
    days = models.IntegerField(null=True)
    tour_place = models.CharField(max_length=100, null=True)
    place_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
            managed = True
