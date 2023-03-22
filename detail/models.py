from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
