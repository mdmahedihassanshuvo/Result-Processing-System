# DJANGO IMPORTS
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, id, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not id:
            raise ValueError('The ID field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, id, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=15, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'full_name']

    def __str__(self):
        return self.email


class UserCategory(models.Model):
    class Category(models.TextChoices):
        STUDENT = 'Student', 'Student'
        TEACHER = 'Teacher', 'Teacher'

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_category'
    )
    category = models.CharField(
        max_length=7,
        choices=Category.choices,
        default=Category.STUDENT,
        db_index=True
    )

    def __str__(self):
        return self.category
