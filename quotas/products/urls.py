from django.conf.urls import url

from .views import Product_list

urlpattern = [
    url('^/<slug>/$', Product_list.as_view(), name='product-details'),
]
