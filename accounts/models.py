from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.mail import send_mail
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

    def create_user(self, email, user_name, password, **other_fields):
        if not email:
            raise ValueError("You must enter a valid email address")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=200)
    about = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    # Delivery details
    country = CountryField()
    address_line1 = models.CharField(max_length=70, blank=True)
    address_line2 = models.CharField(max_length=70, blank=True)
    city_town = models.CharField(max_length=100, blank=True)

    # User Status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'wincommerce.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.email
