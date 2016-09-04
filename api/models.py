from __future__ import unicode_literals
from hasher import hash_password
from django.db import models

class APIUser(models.Model):
    username             = models.TextField(unique=True)
    first_name           = models.TextField(null=True)
    last_name            = models.TextField(null=True)
    email                = models.TextField()
    password             = models.TextField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        super(APIUser, self).save(*args, **kwargs) 

    class Meta:
        db_table = 'api_user'
        verbose_name = 'APIUser'
