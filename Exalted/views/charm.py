# -'- coding: utf-8 -'-
from __future__ import unicode_literals

from braces.views import OrderableListMixin
from ..filters.charm import CharmFilter
from ..forms.charm import *
from ..models.charm import *
from ..models.requirement import *
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q


class CharmIndexView(OrderableListMixin, FilterView):
        model = Charm
        filterset_class = CharmFilter
        template_name = 'charmlist.html'
        orderable_columns = (
                            'charm_name',
                            'charm_essence_min',
                            'requirementset__value',
                            'charm_ex_type__exalted_type_name',
                            'charm_type__name',
                            'charm_duration',
                            'charm_cost_motes',
        )
        context_object_name = 'charms'
        paginate_by = 15


class CharmDetailView(FormView):
    model = Charm
    form = CharmDetailForm
    template_name = 'charmdetails.html'
    context_object_name = 'charm_details'
    '''
    fields = [
              'charm_name',
              'charm_ex_type',
              'charm_duration',
              'charm_type',
              'charm_cost_motes',
              'charm_cost_wp',
              'charm_cost_other',
              'charm_essence_min',
              'charm_no_eclipse',
              'charm_prayer_strip',
              'charm_before',
              'charm_creation',
              'charm_update',
              'charm_tags',
              'tag__name'
              'charm_description',
    ]
    '''


class CharmCreate(CreateView):
    model = Charm
    template_name = 'charmdetails.html'
    fields = [
              'charm_name',
              'charm_ex_type',
              'charm_duration',
              'charm_type',
              'charm_cost_motes',
              'charm_cost_wp',
              'charm_cost_other',
              'charm_essence_min',
              'charm_before',
              'charm_tags',
              'charm_no_eclipse',
              'charm_prayer_strip',
              'charm_tags',
              'charm_description',
    ]
    success_url = reverse_lazy('charm-update', kwargs=[Charm.charm_id])

    def get_success_message(self):
        messages.success(self.request, 'Charm id %s created' % self.object.pk)
        return reverse_lazy('charm-update', kwargs={'pk': self.object.pk})


class CharmUpdate(UpdateView):
    model = Charm
    form = CharmDetailForm
    template_name = 'charmdetails.html'
    fields = [
              'charm_name',
              'charm_ex_type',
              'charm_duration',
              'charm_type',
              'charm_cost_motes',
              'charm_cost_wp',
              'charm_cost_other',
              'charm_essence_min',
              'charm_no_eclipse',
              'charm_prayer_strip',
              'charm_before',
              'charm_tags',
              'charm_description',
    ]
    success_url = reverse_lazy('charm-update')

    def get_success_url(self):
        messages.success(self.request, 'Charm id %s update' % self.object.pk)
        return reverse_lazy('charm-update', kwargs={'pk': self.object.pk})


class CharmDelete(DeleteView):
    model = Charm
    template_name = 'charmdelete_confirm.html'
    success_url = reverse_lazy('charms')

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Charm deleted')
        return super().create(*args,**kwargs)