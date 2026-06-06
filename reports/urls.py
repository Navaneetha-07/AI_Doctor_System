
from django.urls import path
from .views import upload_report,doctor_reports

urlpatterns = [
    path(
        'upload-report/',
        upload_report,
        name='upload_report'
    ),
    path(
    'doctor-reports/',
    doctor_reports,
    name='doctor_reports'
),
]