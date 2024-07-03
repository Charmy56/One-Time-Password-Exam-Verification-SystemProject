from django.contrib import admin
from django.contrib import admin
from .models import Department, Course, UserProfile, Student, Lecturer, Exam, ExamCard, FeeRecord, OTPRecord

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Exam)
admin.site.register(ExamCard)
admin.site.register(FeeRecord)
admin.site.register(OTPRecord)

