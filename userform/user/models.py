from django.db import models

# Create Models for User:

class User_Form(models.Model):
    
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
