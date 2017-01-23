from django.db import models
from django.urls import reverse
from django.conf import settings
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

# Create your models here.


class Printer(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    address = models.CharField(_('Address'), max_length=200)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='printers_profile')
    phone = models.CharField(_('Telephone'), max_length=75, blank=True)
    bio = models.TextField()
    tag_line = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    logo = models.ImageField(upload_to='printers_logos/',
                             null=True,
                             blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Printer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Printer"
        verbose_name_plural = "Printers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('printer-detail', kwargs={'slug': self.slug})
