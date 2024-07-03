# models.py
from django.db import models
from django.contrib.auth.models import User
#from django.contrib import admin
class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/', null=True, blank=False) 
    def __str__(self):
        return self.logo
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_choices = [
        ('Student', 'Student'),
        ('Lecturer', 'Lecturer'),
        ('Exam Admin', 'Exam Admin'),
        ('Finance', 'Finance'),
        ('System Admin', 'System Admin'),
    ]
    role = models.CharField(max_length=20, choices=role_choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    # Add additional user profile information such as role, department, etc.

    def __str__(self):
        return f"{self.user.username}'s Profile"

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
import datetime
class Student(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,  default=1)
    courses = models.ManyToManyField(Course)
    has_paid_fees = models.BooleanField(default=False)
    has_passed_semester_exams = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20) 
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)  # Profile photo field
    #username = models.CharField(max_length=150,  default='DEMOStudent')  # Add username field
    # Other student details

    def __str__(self):
        return self.name

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses_taught = models.ManyToManyField(Course)
    # Other lecturer details

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=False)
    #units = models.ManyToManyField(Unit, related_name='courses')

    def __str__(self):
        return self.name

class Exam(models.Model):
    exam_code = models.CharField(max_length=100, unique=True)
    exam_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    exam_units = models.ManyToManyField(Unit, related_name='exams')
    exam_date = models.DateField()
    # Other exam details

    def __str__(self):
        return self.exam_name

class ExamCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    issued = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=10, blank=True, null=True)
    units = models.ManyToManyField(Unit)
    # Option 1: Provide a one-off default now
    # Add a default value to the year_of_study field in the ExamCard model
    # For example, let's assume the default year of study is 1
    year_of_study = models.PositiveIntegerField(default=2024, blank=True, null=True)
    exam_photo = models.ImageField(upload_to='exam_photos/', null=True, blank=False)

    #def student_profile_photo_url(self):
    #    return self.student.profile_photo.url if self.student.profile_photo else None

    # Other exam card details

    def __str__(self):
        return f"{self.student.name}'s {self.exam.exam_name} Exam Card"

class FeeRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()
    # Other fee record details

    def __str__(self):
        return f"{self.student.name}'s Fee Record"

class OTPRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)
    units = models.ManyToManyField(Unit)
    # Option 1: Provide a one-off default now
    # Add a default value to the year_of_study field in the ExamCard model
    # For example, let's assume the default year of study is 1
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  # Add department field with null=True
    year_of_study = models.PositiveIntegerField(default=2024)

    # Other OTP record details

    def __str__(self):
        return f"{self.student.name}'s OTP Record for {self.exam.exam_name}"
