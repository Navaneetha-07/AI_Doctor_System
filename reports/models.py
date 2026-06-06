from django.db import models
from doctors.models import Doctor

class Report(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    patient_name = models.CharField(max_length=100)

    age = models.IntegerField()

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    symptoms = models.TextField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True
    )

    report_file = models.FileField(
        upload_to='reports/'
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.patient_name