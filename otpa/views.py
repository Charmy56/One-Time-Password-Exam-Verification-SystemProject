from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Exam, ExamCard, OTPRecord, FeeRecord
from .forms import StudentRecordForm, FeeRecordForm, ExamCardForm, Student, AccessOTPForm, GenerateOTPForm
from .models import UserProfile  # Import the UserProfile model
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import random
from django.shortcuts import render, redirect
from .forms import GenerateOTPForm
from .models import OTPRecord

from django.shortcuts import render, redirect
from .forms import GenerateOTPForm
from .models import OTPRecord, Exam, Student  # Import Exam and Student models
from .models import Exam
from .forms import GenerateOTPForm

from django.shortcuts import render
import random
from .forms import GenerateOTPForm
from .models import OTPRecord, Student, Exam

#dashboard 
# views.py
from django.shortcuts import render
from .models import ExamCard
@login_required
def view_exam_cards(request):
    exam_cards = ExamCard.objects.all()
    return render(request, 'view_exam_cards.html', {'exam_cards': exam_cards})

# views.py
from django.shortcuts import render, redirect
from .forms import ExamCardForm
@login_required
def create_exam_card(request):
    if request.method == 'POST':
        form = ExamCardForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            exam_card = form.save()  # Save the form data including the uploaded file
            return redirect('view_exam_cards')
    else:
        form = ExamCardForm()
    return render(request, 'create_exam_card.html', {'form': form})

from django.http import HttpResponse

@login_required
def dashboard(request):
    user_profile = request.user.userprofile
    if user_profile.role == 'System Admin':
        # Redirect to System Admin dashboard
        return redirect('system_admin_dashboard')
    elif user_profile.role == 'Student':
        # Redirect to Student dashboard
        return redirect('student_dashboard')
    elif user_profile.role == 'Exam Admin':
        # Redirect to Exam Admin dashboard
        return redirect('exam_admin_dashboard')
    elif user_profile.role == 'Lecturer':
        # Redirect to Lecturer dashboard
        return redirect('lecturer_dashboard')
    elif user_profile.role == 'Finance':
        # Redirect to Lecturer dashboard
        return redirect('finance_admin_dashboard')
    else:
        # Handle unrecognized roles here, maybe display an error message
        return HttpResponse("Error: Unknown user role.")

@login_required
def system_admin_dashboard(request):
    # Redirect to Django admin page
    return redirect('admin:index')

@login_required
def finance_admin_dashboard(request):
    # Lecturer dashboard logic
    fee_records = FeeRecord.objects.all()
    # Fetch all student records
    student_records = Student.objects.all()

    # Fetch all exam records
    exam_records = Exam.objects.all()
    # System Admin dashboard logic
    return render(request, 'finance_admin_dashboard.html',  {'fee_records': fee_records, 'student_records': student_records, 'exam_records': exam_records})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Logo

@login_required
def student_dashboard(request):
   

    return render(request, 'student_admin_dashboard.html')

@login_required
def exam_admin_dashboard(request):
    # Exam Admin dashboard logic
        # Fetch all OTP records
    otp_records = OTPRecord.objects.all()

    # Fetch all student records
    student_records = Student.objects.all()

    # Fetch all exam records
    exam_records = Exam.objects.all()
    return render(request, 'exam_admin_dashboard.html', {'otp_records': otp_records, 'student_records': student_records, 'exam_records': exam_records})

@login_required
def lecturer_dashboard(request):
    otp_records = OTPRecord.objects.all()
    # Lecturer dashboard logic
    fee_records = FeeRecord.objects.all()
    # Fetch all student records
    student_records = Student.objects.all()

    # Fetch all exam records
    exam_records = Exam.objects.all()
    return render(request, 'lecturer_dashboard.html', {'fee_records': fee_records, 'student_records': student_records, 'exam_records': exam_records, 'otp_records': otp_records})

@login_required
def student_details(request):
    otp_records = OTPRecord.objects.all()
    return render(request, 'student_details.html', {'otp_records': otp_records})
#student views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, OTPRecord
from .forms import StudentRecordForm, GenerateOTPForm

@login_required
def register_student(request):
    if request.method == 'POST':
        form = StudentRecordForm(request.POST)
        if form.is_valid():
            print("Form data:", form.cleaned_data)  # Add this line to print form data for debugging
            form.save()
            messages.success(request, 'Student registered successfully.')
            return redirect('student_dashboard')
    else:
        form = StudentRecordForm()
    return render(request, 'register_student.html', {'form': form})

from django.core.exceptions import ObjectDoesNotExist

def update_profile(request):
    try:
        student = request.user.student
    except ObjectDoesNotExist:
        student = None

    if request.method == 'POST':
        form = StudentRecordForm(request.POST, instance=student)
        if form.is_valid():
            # Check if student object exists before saving
            if student is None:
                # Create a new student object and associate it with the user
                student = form.save(commit=False)
                student.user = request.user
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('student_dashboard')
    else:
        form = StudentRecordForm(instance=student)
    return render(request, 'update_profile.html', {'form': form})


@login_required
def access_otp(request):
    if request.method == 'POST':
        print("Received POST request")
        
        form = AccessOTPForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            otp_code = form.cleaned_data['otp_code']
            try:
                otp_record = OTPRecord.objects.get(otp_code=otp_code)
                print("OTP record found:", otp_record)
                return render(request, 'view_otp.html', {'otp_record': otp_record})
            except OTPRecord.DoesNotExist:
                print("OTP record not found")
                messages.error(request, 'Invalid OTP code.')
                return redirect('access_otp')
        else:
            print("Form errors:", form.errors)  # Print form errors for debugging
            print("Form cleaned data:", form.cleaned_data)  # Print cleaned data for debugging
    else:
        print("Received GET request")
        form = AccessOTPForm()
    return render(request, 'access_otp.html', {'form': form})

'''

@login_required
def generate_otp(request):
    if request.method == 'POST':
        form = GenerateOTPForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            exam_name = form.cleaned_data['exam']

            try:
                student = Student.objects.get(name=student_name)
                exam = Exam.objects.get(exam_name=exam_name)
            except Student.DoesNotExist:
                return render(request, 'generate_otp.html', {'form': form, 'error_message': 'Student not found'})
            except Exam.DoesNotExist:
                return render(request, 'generate_otp.html', {'form': form, 'error_message': 'Exam not found'})

            otp_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            otp_record = OTPRecord.objects.create(student=student, exam=exam, otp_code=otp_code)
            return render(request, 'generate_otp.html', {'form': form, 'success_message': 'OTP generated successfully'})
    else:
        form = GenerateOTPForm()
    
    return render(request, 'generate_otp.html', {'form': form})

'''
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required
def generate_otp(request):
    if request.method == 'POST':
        form = GenerateOTPForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            exam_name = form.cleaned_data['exam']

            try:
                student = Student.objects.get(name=student_name)
                exam = Exam.objects.get(exam_name=exam_name)
            except Student.DoesNotExist:
                return render(request, 'generate_otp.html', {'form': form, 'error_message': 'Student not found'})
            except Exam.DoesNotExist:
                return render(request, 'generate_otp.html', {'form': form, 'error_message': 'Exam not found'})

            otp_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
            otp_record = OTPRecord.objects.create(student=student, exam=exam, otp_code=otp_code)
            
            # Send OTP to student's email
            subject = 'OTP for Exam Access'
            html_message = render_to_string('otp_email_template.html', {'otp_code': otp_code})
            plain_message = strip_tags(html_message)
            from_email = 'otp@valeria.com'  # Enter your email address
            to_email = student.email
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

            return render(request, 'generate_otp.html', {'form': form, 'success_message': 'OTP generated and sent successfully'})
    else:
        form = GenerateOTPForm()
    
    return render(request, 'generate_otp.html', {'form': form})



def login_view(request):
    logo = Logo.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html', {'logo': logo})


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            # Set the role
            user.userprofile.role = role
            user.userprofile.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

from .models import Student, Exam, OTPRecord
'''
@login_required
def dashboard(request):
    # Fetch all OTP records
    otp_records = OTPRecord.objects.all()

    # Fetch all student records
    student_records = Student.objects.all()

    # Fetch all exam records
    exam_records = Exam.objects.all()

    return render(request, 'dashboard.html', {'otp_records': otp_records, 'student_records': student_records, 'exam_records': exam_records})

'''

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OTPRecord

@login_required
def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp_code')
        user = request.user
        user_profile = user.userprofile
        # Check if the user is a system admin, finance personnel, or student  user_profile.role == 'Finance
        if user.is_superuser or user_profile.role == 'Finance' or user_profile.role == 'Student':
            otp_record = OTPRecord.objects.filter(otp_code=otp_entered).first()
            if otp_record:
                if not otp_record.verified:
                    otp_record.verified = True
                    otp_record.save()
                    messages.success(request, 'OTP verified successfully')
                else:
                    messages.warning(request, 'OTP already verified')
            else:
                messages.error(request, 'Invalid OTP')
            return redirect('verify_otp')
        else:
            # Redirect users who do not have permission to verify OTPs
            messages.error(request, 'You do not have permission to verify OTPs.')
            return redirect('permission_denied_page')
    return render(request, 'verify_otp.html')




from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import StudentRecordForm
from django.contrib.auth.decorators import login_required

@login_required
def update_student_records(request):
    user = request.user
    try:
        user_profile = user.userprofile
        
        if request.method == 'POST':
            form = StudentRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Student records updated successfully')
                return redirect('update_student_records')
            else:
                form = StudentRecordForm()
        
            return redirect('dashboard')
    except UserProfile.DoesNotExist:
        messages.error(request, 'User profile does not exist.')
        return redirect('dashboard')

    # Fetch all available messages and pass them to the template
    all_messages = messages.get_messages(request)
    return render(request, 'update_student_records.html', {'form': form, 'messages': all_messages})


from django.contrib import messages

@login_required
def update_fee_records(request):
    user = request.user
    try:
        user_profile = user.userprofile
        if user.is_superuser or user_profile.role == 'Exam Admin' or user_profile.role == 'Finance':
            if request.method == 'POST':
                form = FeeRecordForm(request.POST)
                if form.is_valid():
                    # Process form data and update fee records
                    form.save()
                    messages.success(request, 'Fee records updated successfully')
                    return redirect('update_fee_records')
            else:
                form = FeeRecordForm()
        else:
            messages.error(request, 'Only finance personnel can update fee records.')
            return redirect('dashboard')
    except UserProfile.DoesNotExist:
        messages.error(request, 'User profile does not exist.')
        return redirect('dashboard')

    # Fetch all available messages and pass them to the template
    all_messages = messages.get_messages(request)
    return render(request, 'update_fee_records.html', {'form': form, 'messages': all_messages})




from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExamCardForm
from .models import ExamCard

@login_required
def update_exam_card(request):
    if request.method == 'POST':
        form = ExamCardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exam card updated successfully')
            return redirect('update_exam_card')
        else:
            messages.error(request, 'Failed to update exam card. Please check the form.')
    else:
        form = ExamCardForm()
    
    # Fetch all available messages and pass them to the template
    all_messages = messages.get_messages(request)
    return render(request, 'update_exam_card.html', {'form': form, 'messages': all_messages})


from django.shortcuts import render, redirect, get_object_or_404
from .models import OTPRecord

def view_student_exam_details(request, otp_code):
    try:
        otp_record = OTPRecord.objects.get(otp_code=otp_code)
        if otp_record.verified:
            # OTP is verified, render the student information and exam details
            return render(request, 'student_exam_details.html', {'otp_record': otp_record})
        else:
            # OTP is not verified, display an error message
            return render(request, 'invalid_otp.html', {'error_message': 'Invalid OTP code.'})
    except OTPRecord.DoesNotExist:
        # OTP code does not exist, display an error message
        return render(request, 'invalid_otp.html', {'error_message': 'Invalid OTP code.'})
