from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    is_trailing = models.BooleanField(default=True)
    # add extra fields here
