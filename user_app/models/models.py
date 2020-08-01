from django.db import models
from django.contrib.auth.models import AbstractUser
from user_app.constants.enums import UserRoles


class User(AbstractUser):

    ROLE_CHOICES = [(role.name, role.value) for role in UserRoles]
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    user_role = models.CharField(max_length=20, choices=[(role.name, role.value) for role in UserRoles])
    name = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=300)
