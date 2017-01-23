from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _

from quotas.printers.models import Printer
from quotas.customers.models import Customer

# Create your models here.


class Material(models.Model):
    """
    This list all types material for the quota
    Bond, satinado, opalina, sulfito, polyester
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "material_type"
        verbose_name_plural = "material_types"

    def __str__(self):
        return self.name


class Quota(models.Model):
    # quota itself
    Offset = 'Offset'
    Digital = 'Digital'

    quota_type = (
        (Digital, 'Offset'),
        (Offset, 'Digital'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    before_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    responses_number = models.IntegerField(default=0)
    created_by = models.ForeignKey(Customer)

    quota_type = models.CharField(max_length=50, choices=quota_type)
    material = models.ForeignKey('Material')

    # ask Pietro if custom values are suitables
    size = models.CharField(max_length=50)
    quiebres = models.IntegerField()
    single_side = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Quota")
        verbose_name_plural = _("Quotas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('quota-details', kwargs={'pk': self.pk})


class quota_response(models.Model):
    """ Instance  response for a quota submitted by printer """
    quota = models.ForeignKey(Quota)
    offered_by = models.ForeignKey(Printer)
    cost = models.FloatField()
    deliver_time = models.DateTimeField()
    extra_details = models.TextField()
    has_prepayment = models.BooleanField(default=True)
    prepayment_amount = models.DecimalField(max_digits=4, decimal_places=2)

    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('quota_offer', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = _("quota_response")
        verbose_name_plural = _("quota_responses")

    def __str__(self):
        return self.id
