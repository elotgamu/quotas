from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# from django.db.models.signals import post_save

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='customer_profile')
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=50, choices=gender)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name


# creating the related user
# def create_customer_profile(sender, instance, created, **kwargs):
#        if created:
#           Customer.object.create(user=instance)


# post_save.connect(create_customer_profile, sender=User)
