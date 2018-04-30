# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models


class HealthLevel(models.Model):
    name = models.CharField(max_length=64)
    rating = models.SmallIntegerField()


class HealthLevelSet(models.Model):
    health_levels = models.ManyToManyField(HealthLevel)