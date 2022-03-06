from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import  AbstractBaseUser
# Create your models here.



class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    first_name = models.CharField(_('first_name'),max_length=50,blank=False)
    last_name = models.CharField(_('last_name'),max_length=50,blank=False)
    date_joined = models.DateField(_())