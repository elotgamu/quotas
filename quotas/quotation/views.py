# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quota
from .forms import Quota_Form

# Create your views here.


class Quotas_active_List(ListView):
    model = Quota
    template_name = "quotation/"
    contex_object_name = 'active_quotas'

    def get_queryset(self):
        queryset = super(Quotas_active_List, self).get_queryset()
        return queryset.filter(is_active=True)


class Quota_details(DetailView):
    model = Quota
    template_name = "quotation/quota_details.html"
    contex_object_name = 'quota'


class Quota_Create(LoginRequiredMixin, CreateView):
    model = Quota
    form_class = Quota_Form
    template_name = "quotation/create.html"

    def form_valid(self, form):
        self.object = form.instance
        self.object.created_by = self.user
        return super(Quota_Create, self).form_valid(form)
