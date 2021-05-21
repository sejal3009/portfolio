from django.db import models

# Create your models here.
class student (models.Model):
    firstname = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __str__(self):
       return self.firstname