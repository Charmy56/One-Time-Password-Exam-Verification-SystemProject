'''from django.urls import path
#from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import generate_otp, verify_otp, update_student_records, update_fee_records, update_exam_card, dashboard, register, login_view

urlpatterns = [
    path('generate_otp/', generate_otp, name='generate_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('update_student_records/', update_student_records, name='update_student_records'),
    path('update_fee_records/', update_fee_records, name='update_fee_records'),
    path('update_exam_card/', update_exam_card, name='update_exam_card'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
'''
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('system_admin_dashboard/', views.system_admin_dashboard, name='system_admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('exam_admin_dashboard/', views.exam_admin_dashboard, name='exam_admin_dashboard'),
    path('lecturer_dashboard/', views.lecturer_dashboard, name='lecturer_dashboard'),
    path('register_student/', views.register_student, name='register_student'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('access_otp/', views.access_otp, name='access_otp'),
    path('generate_otp/', views.generate_otp, name='generate_otp'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('update_student_records/', views.update_student_records, name='update_student_records'),
    path('update_fee_records/', views.update_fee_records, name='update_fee_records'),
    path('update_exam_card/', views.update_exam_card, name='update_exam_card'),
    path('finance_admin_dashboard/', views.finance_admin_dashboard , name='finance_admin_dashboard'),
    path('register_student/', views.register_student, name='register_student'),
    path('create_exam_card/', views.create_exam_card, name='create_exam_card'),
    path('view_exam_cards/', views.view_exam_cards, name='view_exam_cards'),
    path('student_details/', views.student_details, name='student_details')
] 
