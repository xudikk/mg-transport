#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager

from common.models import Region


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(username=username, is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        return self.create_user(username, password, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("To'lliq Nomi", max_length=255, null=True)

    username = models.CharField(max_length=50, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    lang = models.CharField(default='uz', max_length=2, choices=[("uz", 'uz'), ("ru", 'ru'), ("en", 'en')])
    ut = models.SmallIntegerField(verbose_name="User Type", default=3, choices=[
        (1, 'Super Admin'),
        (2, "Admin"),
    ])  # user type

    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_("Tegishli Viloyat"),
                               related_name="user_region")

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, editable=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['ut', 'region_id']

    class Meta:
        verbose_name_plural = "1. Users"

    def full_name(self):
        return f"{self.name} | {self.username}"

    def personal(self):
        ut = {1: 'Super Admin',
              2: "Admin",
              }[self.ut]
        return {
            'name': self.name,
            'lang': self.lang,
            'user_type': ut,
            "username": self.username,
            "region": self.region.name,
        }
