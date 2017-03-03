# from django.shortcuts import render

from django.views.generic import ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
# Create your views here.


class Product_list(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = 'products'


class Product_detail(DetailView):
    model = Product
    template_name = "product/product_detail.html"
