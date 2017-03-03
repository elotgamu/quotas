# from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer
from .forms import CustomerForm

# Create your views here.


class Customer_Create(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/create_customer.html"
    form_class = CustomerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Customer_Create, self).form_valid(form)


class Customer_List(ListView):
    model = Customer
    template_name = "customers/customers_list.html"
    context_object_name = 'customers'
