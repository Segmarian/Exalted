# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models


class Artifact(models.Model):
    name = models.CharField(max_length=90)
    rating = models.SmallIntegerField(null=True, )

    def __str__(self):
        return '%s' % self.name
