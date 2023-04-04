from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *


class User(AbstractUser):
    username = None
    email = models. EmailField(unique=True)
    profile_image = models.ImageField(upload_to='static/profile_images/', null=True, blank=True)
    contact_no = models. CharField (max_length=12)
    
    USER_ROLES = (
        ('C', 'Customer'),
        ('S', 'Seller')
    )
    user_role = models.CharField(max_length=1, choices=USER_ROLES, default='C')
    email_token = models.CharField(max_length=36)
    is_active = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    