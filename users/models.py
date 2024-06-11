from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from config.models import BasedModel

class User(AbstractUser,BasedModel):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
