from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(models.Model):
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    encrypted_mobile = models.CharField(max_length=1024)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)

    def __str__(self):
        return self.name + " " + self.mobile
