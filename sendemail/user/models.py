from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    #abstractuser by default password er shob kichu kore
    username= None
    email= models.EmailField(_('Email Address'), max_length=50, unique= True)
    password= models.CharField(max_length=30)
    email_is_verified= models.BooleanField(default= False)
    
    USERNAME_FIELD= 'email' #ar username lagbe na
    REQUIRED_FIELDS= []
    
    objects= CustomUserManager() #to customize how queries are performed on instances of that model.
    
    def __str__(self) -> str:
        return self.email
    
    
    #ekta new instance create or update howar por ki korte hobe shetar control pabo
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        

