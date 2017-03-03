from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Weight(models.Model):
    """
    This is regard the weight of the material to use
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Weight"
        verbose_name_plural = "Weights"

    def __str__(self):
        self.name


class Material(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    peso = models.ForeignKey(Weight, related_name='Gramaje')

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_pliegos = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)
    material = models.ForeignKey(Material, related_name='Material')
    slug = models.SlugField()

    created_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='Added_by')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product-details', args=[str(self.slug)])
