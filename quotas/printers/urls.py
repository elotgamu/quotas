from django.conf.urls import url

from .views import Printer_Create, Printer_Detail


# Printers related urls goes here


urlpatterns = [
    url(r'^add/', Printer_Create.as_view(), name='printer-add'),
    url(r'^details/(?P<slug>[\w\-]+)/$', Printer_Detail.as_view(),
        name='printer-detail'),
]
