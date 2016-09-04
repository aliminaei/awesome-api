from __future__ import unicode_literals
from django.db import models

class API_User(models.Model):
    username             = models.TextField(unique=True)
    first_name           = models.TextField()
    last_name            = models.TextField()
    email                = models.TextField()
    password             = models.TextField()
