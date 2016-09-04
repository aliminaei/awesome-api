from __future__ import unicode_literals
from hasher import hash_password
from django.db import models

class API_User(models.Model):
    username             = models.TextField()
    first_name           = models.TextField()
    last_name            = models.TextField()
    email                = models.TextField()
    password             = models.TextField()

    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        super(API_User, self).save(*args, **kwargs) 
