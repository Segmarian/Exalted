# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models


class Tag_category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name


class Tag(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Tag_category, related_name='tag', on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s' % self.name