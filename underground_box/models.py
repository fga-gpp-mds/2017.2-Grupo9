from django.db import models
from emendation_box.models import EmendationBox
from technical_reserve.models import TechnicalReserve


class UndergroundBoxType(models.Model):
    name = models.CharField(blank=True, max_length=100)


class UndergroundBox(models.Model):
    code = models.CharField(max_length=200, blank=False, default='none',
                            unique=True)
    box_type = models.ForeignKey(UndergroundBoxType, null=False)
    lattitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    cover_type = models.CharField(max_length=20, blank=True, null=True)
    emendation_box = models.ForeignKey(EmendationBox, null=True)
    technical_reserve = models.ForeignKey(TechnicalReserve, null=True)
