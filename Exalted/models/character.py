# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models
from .exalted_type import Exalted_type, Exalted_subtype
from .healthlevel import HealthLevelSet


class Location(models.Model):
    location_name = models.CharField(max_length=90)

    def __str__(self):
        return '%s' % self.name


class Character(models.Model):
    class Meta:
        db_table='character'
    character_name = models.CharField(max_length=90)
    character_exalted_type = models.ForeignKey(Exalted_type, on_delete=models.PROTECT, null=True,)
    character_essence = models.SmallIntegerField( null=True,)
    character_exalted_subtype = models.ForeignKey(Exalted_subtype, on_delete=models.PROTECT, null=True,)
    character_health_level_set = models.ForeignKey(HealthLevelSet, on_delete=models.CASCADE, null=True,)
    character_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True,)

    def __str__(self):
        return '%s' % self.name
