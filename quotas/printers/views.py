# from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from .models import Printer

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"
    model = Printer
    context_object_name = 'printers'


class Printer_Create(CreateView):
    model = Printer
    template_name = "TEMPLATE_NAME"


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
