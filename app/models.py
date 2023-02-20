from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManger(BaseUserManager):
    def create_user(self, email, password, is_staff=False, is_active=True, is_admin=False):
        if not email:
            raise ValueError("User must have email address")
        if not password:
            raise ValueError("User must have password")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.staff = is_staff
        user.active = is_active
        user.admin = is_admin

        user.save(using=self._db)
        return user

    def create_staff_user(self, email, password):
        user = self.create_user(email, password, is_staff=True)
        return user

    def create_admin_user(self, email, password):
        user = self.create_user(email, password,  is_staff=True, is_admin=True)
        return user


class SUser(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    USER_NAME = 'email'

    def __str__(self):
        return self.enroll

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    degree = models.CharField(max_length=10)
    branch = models.CharField(max_length=30)
    contact = models.IntegerField(null=True, blank=True)


class Registration(models.Model):
    enroll = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    degree = models.CharField(max_length=10)
    branch = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.enroll
    # contact = models.IntegerField(null=True, blank=True, default=None)


# Create your models here.
