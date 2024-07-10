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
from otpa.models import Exam, Course, Lecturer, Department, Unit
from django.contrib.auth.models import User

fake = Faker('en_US')

def create_courses():
    print("Creating courses...")
    department = Department.objects.order_by('?').first()
    for _ in range(7):  # Generate 7 courses
        course_name = fake.random_element(elements=('Computer Science', 'Mathematics', 'Physics', 'Business', 'English', 'Chemistry', 'Arts'))
        course_code = fake.unique.random_number(digits=3)  # Generate a unique course code
        Course.objects.get_or_create(name=course_name, code=course_code, department=department)
    print("All courses created successfully.")

def create_exams(num_exams=20):
    print("Creating exams...")
    exams_created = 0
    courses = list(Course.objects.all())
    lecturers = list(Lecturer.objects.all())
    while exams_created < num_exams:
        course = random.choice(courses)
        lecturer = random.choice(lecturers)
        exam_code = fake.unique.random_number(digits=4)  # Generate a unique exam code
        exam_name = fake.text(max_nb_chars=50)
        exam_date = fake.date_time_between(start_date='-30d', end_date='+30d', tzinfo=None)
        exam, created = Exam.objects.get_or_create(
            exam_code=exam_code,
            exam_name=exam_name,
            course=course,
            lecturer=lecturer,
            exam_date=exam_date,
        )
        if created:
            exams_created += 1
            print(f"Creating exam {exams_created}/{num_exams}")
    print("All exams created successfully.")
def create_units(num_units=40):
    units_created = 1
    while units_created < num_units:
        id = fake.unique.random_number(digits=2)
        name = fake.text(max_nb_chars=30)
        code = fake.unique.random_number(digits=4)
        Unit.objects.update_or_create(id=id, name=name, code=code)


if __name__ == '__main__':
    #create_courses()
    #create_exams()
    create_units()
