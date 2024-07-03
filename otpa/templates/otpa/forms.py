from django import forms
from .models import Student, FeeRecord, ExamCard

class StudentRecordForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'email', 'phone_number', 'has_paid_fees', 'has_passed_semester_exams']  # Add fields as needed
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'has_paid_fees': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_passed_semester_exams': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ['student', 'amount', 'date_paid']  # Add fields as needed
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_paid': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ExamCardForm(forms.ModelForm):
    class Meta:
        model = ExamCard
        fields = ['student', 'exam', 'issued', 'otp_code']  # Add fields as needed
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'issued': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'otp_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
