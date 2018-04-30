from __future__ import unicode_literals

from django.db import models


class KungfuCircle(models.Model):
    name = models.CharField(max_length=64, )

    def __str__(self):
        return '%s' % self.name


class MagicCircle(models.Model):
    name = models.CharField(max_length=64, )

    def __str__(self):
        return '%s' % self.name


class HealthLevels(models.Model):
    name = models.CharField(max_length=64, )
    value = models.SmallIntegerField()

    def __str__(self):
        return '%s' % self.name


class FavoredItems(models.Model):
    name = models.CharField(max_length=64, )

    def __str__(self):
        return '%s' % self.name


class Exalted_type(models.Model):
    exalted_type_name = models.CharField(max_length=64, )
    exalted_type_available_magic = models.ManyToManyField(MagicCircle, related_name="+", )
    exalted_type_available_kungfu = models.ManyToManyField (KungfuCircle, related_name="+", )
    exalted_type_health_level = models.ForeignKey(HealthLevels, related_name="+", on_delete=models.PROTECT, null=True,)
    exalted_type_ability_cost = models.SmallIntegerField(null=True,)
    exalted_type_attribute_cost = models.SmallIntegerField(null=True,)
    exalted_type_charm_cost = models.SmallIntegerField(null=True,)
    exalted_type_essence_cost = models.SmallIntegerField(null=True,)
    exalted_type_extended_charm_cost = models.SmallIntegerField(null=True,)
    exalted_type_favored_cost = models.SmallIntegerField(null=True,)
    exalted_type_favored_type = models.ForeignKey(FavoredItems, null=True, on_delete=models.PROTECT, )
    exalted_type_favored_modifier = models.SmallIntegerField(null=True,)

    def __str__(self):
        return '%s' % self.exalted_type_name


class Exalted_subtype(models.Model):
    exalted_subtype_exalted_type = models.ForeignKey(Exalted_type,null=True, on_delete=models.PROTECT,)
    exalted_subtype_name = models.CharField(max_length=64,null=True, )
    exalted_subtype_eclipse = models.NullBooleanField(null=True,)
    exalted_subtype_health_level = models.ForeignKey(HealthLevels, related_name="+",null=True, on_delete=models.PROTECT,)

    def __str__(self):
        return '%s' % self.exalted_subtype_name

