# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from django.db import models
from .exalted_type import Exalted_type
from .tag import Tag


class Charm_type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s' % self.name


class Charm(models.Model):

    class Meta:
        db_table='charm_data'
        ordering = ['charm_essence_min', 'requirementset']
    charm_id = models.IntegerField(primary_key=True)
    charm_name = models.CharField(max_length=90,
                                  verbose_name=u"Name",
                                  )
    charm_ex_type = models.ForeignKey(Exalted_type,
                                      on_delete=models.PROTECT,
                                      null=True,
                                      blank=True,
                                      related_name="exalted",
                                      verbose_name = u"Exalted",
                                      )
    charm_duration = models.CharField(max_length=64,
                                      null=True,
                                      blank=True,
                                      verbose_name = u"Duration",
                                      )
    charm_type = models.ForeignKey(Charm_type,
                                   on_delete=models.PROTECT,
                                   null=True,
                                   blank=True,
                                   related_name="type",
                                   verbose_name = u"Type",
                                   )
    charm_cost_motes = models.SmallIntegerField(null=True,
                                                blank=True,
                                                verbose_name = u"Motes",
                                                )
    charm_cost_wp = models.SmallIntegerField(null=True,
                                             blank=True,
                                             verbose_name = u"Willpower",
                                             )
    charm_cost_other = models.CharField(max_length=64, null=True,
                                        blank=True,
                                        verbose_name = u"Other cost",
                                        )
    charm_essence_min = models.SmallIntegerField(null=True,
                                                 blank=True,
                                                 verbose_name = u"Essence",
                                                 )
    charm_no_eclipse = models.NullBooleanField(null=True,
                                               blank=True,
                                               verbose_name = u"Not learnable by Eclipse",
                                               )
    charm_prayer_strip = models.NullBooleanField(null=True,
                                                 blank=True,
                                                 verbose_name = u"Requires prayer strip",
                                                 )
    charm_description = models.TextField(verbose_name = u"Description",)
    charm_before = models.ManyToManyField("self",
                                          related_name="charm_before",
                                          verbose_name = u"Preceding charm",
                                          null=True,
                                          blank = True,
                                          )
    charm_creation = models.DateTimeField(auto_now_add=True,
                                          verbose_name = u"Created",
                                          )
    charm_update = models.DateTimeField(auto_now=True,
                                        verbose_name = u"Updated",
                                        )

    charm_tags = models.ManyToManyField(Tag,
                                        related_name="tags",
                                        verbose_name = u"Tags",
                                        blank=True,
                                        )

    def __str__(self):
        return '%s %s' %(self.charm_id, self.charm_name)