from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

# from quotas.users import User

# Create your models here.


class Customer(models.Model):
    gender = (
        ('M', '_(Male)'),
        ('F', '_(Female)'),
    )
    gender = models.CharField(max_length=50, choices=gender)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='customer_profile')

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.first_name + self.last_name
