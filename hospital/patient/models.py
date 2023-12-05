from django.db import models

class Patient(models.Model):

    GENDERS_CHOISE = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDERS_CHOISE, max_length=20),

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
