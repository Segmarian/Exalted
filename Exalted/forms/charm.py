# -'- coding: utf-8 -'-
from __future__ import unicode_literals
from django_filters import *
from django_filters.widgets import *
from django.forms import *
from ..models.charm import Charm, Charm_type
from ..models.exalted_type import Exalted_type
from django.db.models import Q, F
from ..filters.charm import *
from ..models.tag import Tag, Tag_category
from ..models.requirement import RequirementSet, Requirement, RequirementType


class CharmDetailForm(Form):
    class Meta:
        model = Charm
        exclude = ["charm_id", "charm_before"]

    field_order = ['charm_name']

    charm_ex_type__exalted_type_name = ModelChoiceField(
        Exalted_type,
        widget=widgets.Select(),
        required=False)

    charm_before = ModelMultipleChoiceField(
        Charm,
        widget=CheckboxSelectMultiple(),
        to_field_name="charm_name"
        )

'''
    def req_name_filter(self, queryset, name, req_name):
        return queryset.filter(Q(requirementset__name__icontains=req_name))

    requirementset__requirement__name = \
        ModelChoiceFilter(
            queryset=Requirement.objects.all(),
            method='req_name_filter',
            label="Requirement",
            widget=Select()
        )

    
    requirementset = NumberFilter(
        label="Value",
    )


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

    

    def req_value_filter(self, queryset, name, req_name):
        for req in req_name:
            args = args |Q(value__lte=req)
        return queryset.filter(args)
'''