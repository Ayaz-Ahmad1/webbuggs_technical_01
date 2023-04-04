from django.contrib.auth.models import AbstractUser
from accounts.models import User
from django.db import models
from django.contrib.auth import get_user_model
from softdelete.models import SoftDeleteModel
import uuid
#from users.models import User


class ProductCategory(SoftDeleteModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/product_category_images', null=True, blank=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='created_categories', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class SubCategory(SoftDeleteModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, related_name='SubCategory', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/sub_category_images', null=True, blank=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='created_subcategories', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_subcategories', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Color(SoftDeleteModel):
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Product(SoftDeleteModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    color = models.ManyToManyField(Color)
    description = models.TextField()
    sku = models.CharField(max_length=100, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='created_products', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='updated_products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = f"prod-{self.created_at}-{self.pk}"
        super().save(*args, **kwargs)

