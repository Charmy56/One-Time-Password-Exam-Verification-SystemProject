import os
import sys
import random
from faker import Faker
from datetime import datetime, timedelta

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VALP.settings")
sys.path.append(os.path.abspath("C:\\Users\\Sana\\Desktop\\VALP\\VALP"))
import django
django.setup()

# Import models
from otpa.models import Student, Exam, Course, Lecturer, Department, FeeRecord
from django.contrib.auth.models import User

fake = Faker('en_US')

def create_departments(num_departments=5):
    for _ in range(num_departments):
        department_name = fake.word()
        Department.objects.create(name=department_name)

def create_students(num_students=20):
    departments = Department.objects.all()
    for _ in range(num_students):
        # Generate a fake user
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)
        user = User.objects.create_user(username=username, email=email, password=password)

        # Generate a fake student
        student_id = fake.random_int(min=1000, max=9999)
        name = fake.name()
        phone = fake.phone_number()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=25)
        address = fake.address()
        department = random.choice(departments)  # Choose a random department
        phone_number = fake.phone_number()

        # Create the student
        student = Student.objects.create(
            user=user,
            student_id=student_id,
            name=name,
            email=email,
            phone=phone,
            date_of_birth=date_of_birth,
            address=address,
            department=department,
            phone_number=phone_number,
        )

        # Create fee record for the student
        amount = fake.random_int(min=1000, max=5000)
        date_paid = fake.date_this_decade()
        FeeRecord.objects.create(student=student, amount=amount, date_paid=date_paid)

def create_exams(num_exams=20):
    for _ in range(num_exams):
        # Generate a fake course
        course_code = fake.random_element(elements=('CS101', 'MATH101', 'PHY101', 'BUS543'))
        course_name = fake.random_element(elements=('Computer Science', 'Mathematics', 'Physics', 'Business'))
        course = Course.objects.create(course_code=course_code, course_name=course_name)

        # Generate a fake lecturer
        lecturer_name = fake.name()
        lecturer_email = fake.email()
        lecturer = Lecturer.objects.create(name=lecturer_name, email=lecturer_email)

        # Generate a fake exam
        exam_code = fake.random_int(min=1000, max=9999)
        exam_name = fake.text(max_nb_chars=50)
        exam_date = fake.date_time_between(start_date='-30d', end_date='+30d', tzinfo=None)
        exam = Exam.objects.create(
            exam_code=exam_code,
            exam_name=exam_name,
            course=course,
            lecturer=lecturer,
            exam_date=exam_date,
        )

if __name__ == '__main__':
    create_departments()
    create_students()
    create_exams()
