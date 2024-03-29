from django.db import models

# Create Models for User-Form:

class UserRegistration(models.Model):
    
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
