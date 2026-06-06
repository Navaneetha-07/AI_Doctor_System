from django import forms
from .models import Report

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report

        fields = [
            'patient_name',
            'age',
            'gender',
            'symptoms',
            'doctor',
            'report_file'
        ]

        widgets = {

            'patient_name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Patient Name'
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter Age'
                }
            ),

            'gender': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

            'symptoms': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'rows':4,
                    'placeholder':'Describe Symptoms'
                }
            ),

            'doctor': forms.Select(
                attrs={
                    'class':'form-select'
                }
            ),

            'report_file': forms.FileInput(
                attrs={
                    'class':'form-control'
                }
            ),
        }