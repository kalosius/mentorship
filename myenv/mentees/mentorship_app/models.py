from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    DOB  = models.DateField()

    def __str__(self):
        return self.name
       