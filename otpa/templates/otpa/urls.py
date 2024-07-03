from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import generate_otp, verify_otp, update_student_records, update_fee_records, update_exam_card, dashboard

urlpatterns = [
    path('generate_otp/', generate_otp, name='generate_otp'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('update_student_records/', update_student_records, name='update_student_records'),
    path('update_fee_records/', update_fee_records, name='update_fee_records'),
    path('update_exam_card/', update_exam_card, name='update_exam_card'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
