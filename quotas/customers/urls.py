from django.conf.urls import url

from .views import Customer_Create, Customer_List

urlpatterns = [
    url(r'^list/$', Customer_List.as_view(), name='customer-list'),
    url(r'^create/$', Customer_Create.as_view(), name='new_customer'),
]
