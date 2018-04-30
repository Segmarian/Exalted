# -'- coding: utf-8 -'-
from __future__ import unicode_literals
from django_filters import *
from django_filters.widgets import *
from django.forms import *
from ..models.charm import Charm, Charm_type
from ..models.requirement import RequirementSet, RequirementType, Requirement
from ..models.exalted_type import Exalted_type, Exalted_subtype
from django.db.models import Q, CharField
from django import template
register = template.Library()


class CharmFilter(FilterSet):
    class Meta:
        model = Charm
        fields = {
                  'charm_type__name': ['icontains' ],
                  'charm_duration': ['icontains',],
                  'charm_cost_motes': ['gte',],
                  'charm_cost_wp': ['gte', ],
                  'charm_cost_other': ['icontains',],
                  'charm_essence_min': ['lte',],
                  'charm_update': ['gte'],
                  }


    charm_name = CharFilter(
        label="Charm name",
        method="name_filter",
    )

    charm_ex_type__exalted_type_name = ModelChoiceFilter(
        label="Exalted",
        queryset=Exalted_type.objects.all()
    )

    requirementset__requirement = \
        ModelChoiceFilter(
            queryset=Requirement.objects.all(),
            method='req_name_filter',
            label="Requirement",
        )

    '''
    requirementset = NumberFilter(
        label="Value",
    )
    '''

    charm_type__name = ModelChoiceFilter(
        label="Type",
        queryset = Charm_type.objects.all(),
    )

    charm_no_eclipse = BooleanFilter(
        label="Not learnable by Eclipse",
        widget = BooleanWidget()
        )

    charm_prayer_strip = BooleanFilter(
        label="Requires prayer strip",
        widget=BooleanWidget()
    )

    def name_filter(self, queryset, name, cname):
        return queryset.filter(Q(charm_name__icontains=cname)| Q(charm_description__icontains=cname))

    def req_name_filter(self, queryset, name, req_name):
        return queryset.filter(Q(requirementset__requirement__name = req_name))
'''
    def req_value_filter(self, queryset, name, req_name):
        for req in req_name:
            args = args |Q(value__lte=req)
        return queryset.filter(args)
'''


class CharmViewFilter(CharmFilter):
    charm_before = ModelMultipleChoiceFilter(
        label='Previous charms',
        queryset=Charm.objects.all(),
        widget=CheckboxSelectMultiple(),
        method='charm_before_filter',
    )

    def __init__(self):
        super(CharmFilter, self).__init__()

    def charm_before_filter(self, queryset, name, value):
        return queryset.filter(Q(charm_before__charm__charm_id, icontains=value))

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})