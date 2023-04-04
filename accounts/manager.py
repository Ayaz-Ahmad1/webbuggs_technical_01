from django.contrib.auth.base_user import BaseUserManager
from .send_mail import _send_mail_to_users
import uuid
from django.utils import timezone



class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email,  password=None, email_token=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        email_token = str(uuid.uuid4())
        user = self.model(email = email,email_token=email_token, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault ('is_active' ,False)
        user.save(using=self._db)
        
        _send_mail_to_users(email, email_token)
        return user

    def create_superuser(self , email , password = None, email_token=None, **extra_fields):
        extra_fields.setdefault ('is_staff' , True )
        extra_fields.setdefault ('is_superuser' , True)
        return self.create_user (email , password ,email_token, **extra_fields)
    

