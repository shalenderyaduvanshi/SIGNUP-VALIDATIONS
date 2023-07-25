from django.db import models


# Create your models here.

class user(models.Model):
    objects = None
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.BigIntegerField()
    Password = models.CharField(max_length=50)

    class Meta:
        db_table = 'user'
