from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=30, blank=True)
    mail_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
