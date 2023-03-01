from django.utils import timezone

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from app.models import Course


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('1', 'Student'),
        ('2', 'Doctor'),
        ('3', 'Admin'),
    )

    objects = UserManager()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES)
    courses = models.ManyToManyField(Course)
    username = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def find_by_username(self, name):
    #     return self.objects.filter(username=name)
    #
    # def find_by_id(self, id):
    #     return self.objects.filter(id=id)
