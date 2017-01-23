from django.conf.urls import url

from .views import Quotas_active_List, Quota_details, Quota_Create

# Quotas related url

urlpatterns = [
    url(r'^actives/', Quotas_active_List.as_view(), name='active-quotas'),
    url(r'^details/(?P<pk>\d+)', Quota_details.as_view(),
        name='quota-details'),
    url(r'^create/', Quota_Create.as_view(), name='submit-quota'),
]
