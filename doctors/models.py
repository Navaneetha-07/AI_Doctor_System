from django.db import models

class Doctor(models.Model):

    CATEGORY_CHOICES = [
        ('General Physician', 'General Physician'),
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Orthopedic', 'Orthopedic'),
    ]

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    experience = models.IntegerField()

    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name