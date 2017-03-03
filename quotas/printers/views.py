# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Printer
from .forms import Printercreation_form

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"
    model = Printer
    context_object_name = 'printers'


class Printer_Create(LoginRequiredMixin, CreateView):
    model = Printer
    form_class = Printercreation_form
    template_name = "printers/printer_create.html"

    def get_form_kwargs(self):
        kwargs = super(Printer_Create, self).get_form_kwargs()
        kwargs['email'] = self.request.user.email
        return kwargs

    def form_valid(self, form):
        self.form.user = self.request.user
        return super(Printer_Create, self).form_valid(form)


class Printer_Detail(DetailView):
    model = Printer
    template_name = "printers/detail_printer.html"


class PrintersList(ListView):
    """Just to see all printers"""
    model = Printer
    context_object_name = 'printer'

    def __init__(self, arg):
        super(PrintersList, self).__init__()
        self.arg = arg
