# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models
from .charm import Charm


class RequirementType(models.Model):
    name = models.CharField(max_length=64, verbose_name=u"Requirement type",)

    def __str__(self):
        return '%s' % self.name


class Requirement(models.Model):
    name = models.CharField(max_length=64,
                            verbose_name=u"Requirement",
                            )
    type = models.ForeignKey(RequirementType,
                             related_name='requirement',
                             on_delete=models.DO_NOTHING,
                             null=True,
                             verbose_name=u"Requirement type",
                             )

    def __str__(self):
        return '%s' % self.name


class RequirementSet(models.Model):
    class Meta:
        ordering = ['requirement','value']
    charm = models.ForeignKey(Charm, on_delete=models.PROTECT, related_name='requirementset', verbose_name=u"Charm with requirement",)
    requirement = models.ForeignKey(Requirement, on_delete=models.PROTECT, related_name ='requirementset', null=True, verbose_name=u"part of Requirement",)
    value = models.SmallIntegerField(verbose_name=u"Value of requirement",)

    def __str__(self):
        return '%s %s %s' % (self.charm, self.requirement, self.value)
