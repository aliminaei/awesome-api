from __future__ import unicode_literals
from hasher import hash_password
from django.db import models

class APIUser(models.Model):
    username             = models.CharField(primary_key=True, unique=True, max_length=254)
    first_name           = models.CharField(null=True, blank=True, max_length=254)
    last_name            = models.CharField(null=True, blank=True, max_length=254)
    email                = models.EmailField(max_length=254)
    password             = models.CharField(max_length=254)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = hash_password(self.password)
        super(APIUser, self).save(*args, **kwargs) 

    class Meta:
        db_table = 'api_user'
        verbose_name = 'APIUser'
