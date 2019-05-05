from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, pre_save
from django.urls import reverse

from ecommerce.utils import unique_slug_generator

# Create your models here.
class CustomManager(models.Manager):
    def featured(self):
        return super().get_queryset().filter(featured=True)

    def search(self,query):
        lookups =(Q(title__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query) | Q(tag__title__icontains=query))
        return super().get_queryset().filter(lookups).distinct()
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug  = models.SlugField(blank=True,default='abc',unique=True)
    description = models.TextField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = CustomManager()
    def get_absolute_url(self):
        # return "/products/{slug}/ ".format(slug=self.slug)
        return reverse("product" , kwargs={"slug":self.slug})

    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,  sender=Product)
