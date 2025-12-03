from django.db import models
from django.utils.text import slugify
from baseapp.models import BaseModel


class Category(BaseModel):
    name = models.CharField(null=False, blank=False, max_length=100)
    slug = models.SlugField(null=False, blank=False, unique=False)
    image = models.ImageField(upload_to="media/images")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya_"


class Product(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    cost = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(upload_to='media/products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mahsulotlar_"




