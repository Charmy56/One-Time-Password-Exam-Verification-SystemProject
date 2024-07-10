import os
import sys
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VALP.settings")
sys.path.append(os.path.abspath("C:\\Users\\Sana\\Desktop\\VALP\\VALP"))
import django
django.setup()

# Import models
from otpa.models import Student, Exam, Course, Lecturer, Department, FeeRecord
from django.contrib.auth.models import User

fake = Faker('en_US')

def generate_unique_student_id():
    while True:
        student_id = fake.random_int(min=1000, max=9999)
        if not Student.objects.filter(student_id=student_id).exists():
            return student_id

def create_students(num_students=20):
    departments = Department.objects.all()
    for _ in range(num_students):
        # Generate other fake student details
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)
        user = User.objects.create_user(username=username, email=email, password=password)

        name = fake.name()
        phone = fake.phone_number()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=25)
        address = fake.address()
        department = random.choice(departments)
        phone_number = fake.phone_number()

        # Generate a unique student ID
        student_id = generate_unique_student_id()

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

if __name__ == '__main__':
    create_students()
    print("created")
