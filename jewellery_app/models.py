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
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    maincategory = models.CharField(max_length=200, null=True, blank=True)
    subcategory1 = models.CharField(max_length=200, null=True, blank=True)
    subcategory2 = models.CharField(max_length=200, null=True, blank=True)
    subcategory3 = models.CharField(max_length=200, null=True, blank=True)
    subcategory4 = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.maincategory
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_thumb = models.ImageField(upload_to='product_thumb/')
    product_thumb_act = models.CharField(max_length=200, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_name', null=True, blank=True)
    subcategory_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory_name', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.product_name



# class Subcategory(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title


# class Category(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

# class Midimg(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     subtitle = models.CharField(max_length=200)
#     img = models.ImageField(upload_to="midimg/")
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
