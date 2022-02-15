from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        if other_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned is_active=True status')
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned is_staff=True status')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned is_superuser=True status')
        return self.create_user(email, user_name, password, **other_fields)


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.email(_('email'), unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    # Delivery details
    country = CountryField()
    address_line1 = models.CharField(max_length=70, blank=True)
    address_line2 = models.CharField(max_length=70, blank=True)
    city_town = models.CharField(max_length=100, blank=True)
    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email
