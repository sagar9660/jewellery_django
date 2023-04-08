from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from PIL import Image

# Create your models here.

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='slider/', null=True, blank=True)
    # featured = models.ImageField(upload_to='featured/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title