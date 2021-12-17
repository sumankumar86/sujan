from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

DeptChoice = [
    ('', 'Depertment'),
    ('Not Applicable', 'Not Applicable'),
    ('Mechanical', 'Mechanical'),
    ('Civil', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
]
YearChoice = [
    ('', 'Year'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstYear', 'First Year'),
    ('SecondYear', 'Second Year '),
    ('ThirdYear', 'Third Year'),
    ('FourthYear', 'Fourth Year'),
]
SemChoice = [
    ('', 'Semester'),
    ('Not Applicable', 'Not Applicable'),
    ('FirstSemester', 'First Semester'),
    ('SecondSemester', 'Second Semester '),
    ('ThirdSemester', 'Third Semester'),
    ('FourthSemester', 'Fourth Semester'),
    ('FifthSemester', 'Fifth Semester'),
    ('SixthSemester', 'Sixth Semester'),
    ('SeventhSemester', 'Seventh Semester'),
    ('EighthSemester', 'Eighth Semester'),
]

SubjectChoice = [
    # Five Paper from each Streem
    ("Mathematics", "Mathematics"),
    ("Data Structure & Algorithms", "Data Structure & Algorithms"),
    ("Circuit Theory & Networks", "Circuit Theory & Networks"),
    ("Computer Organisation", "Computer Organisation"),
    ("Digital Electronics & Logic Design", "Digital Electronics & Logic Design"),
    ("Principles of Programming Language", "Principles of Programming Language"),
    ("Formal Language & Automata Theory", "Formal Language & Automata Theory"),
    ("Operation Research & Optimization Techniques",
     "Operation Research & Optimization Techniques"),
    ("Principles of Communication Engg", "Principles of Communication Engg"),
    ("Advanced Computer Architecture", "Advanced Computer Architecture"),
    ("Operating System", "Operating System"),
    ("Database Management System", "Database Management System"),
    ("Design & Analysis of Algorithm", "Design & Analysis of Algorithm"),
    ("Microprocessor & Microcontrollers", "Microprocessor & Microcontrollers"),
    ("Control System", "Control System"),
    ("Computer network", "Computer network"),
    ("Software Engineering", "Software Engineering"),
    ("Computer Graphics & Multimedia", "Computer Graphics & Multimedia"),
    ("System Software and Administration", "System Software and Administration"),
    ("Object Technology & UML", "Object Technology & UML"),
    ("Language  Processor", "Language  Processor",),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Visual Programming and Web technology",
     "Visual Programming and Web technology"),
    ("Financial Management and accounts", "Financial Management and accounts"),
]

NewsDeptChoice = [
    ('Mechanical', 'Mechanical'),
    ('Civil ', 'Civil '),
    ('Electrical', 'Electrical'),
    ('ComputerScience', 'Computer Science'),
    ('Electronics&Communication', 'Electronics & Communication'),
    ('placement', 'Placement'),
    ('admission', 'Admission'),
    ('event', 'Event'),
    ('CDC', 'CDC'),
]
Pincategory = [
    ('Campus', 'Campus'),
    ('Carrer', 'Carrer'),
    ('Culture', 'Culture'),
    ('Sports', 'Sports'),
    ('Student', 'Student'),
    ('Teacher', 'Teacher'), ]


class User(AbstractUser):
    # Need For All Project
    dept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    year = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    semester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    enrollment = models.CharField(max_length=70, null=True, blank=True)
    profilepic = models.ImageField(
        upload_to='profile_pic/', null=True, blank=True, default='https://res.cloudinary.com/mern-commerce/image/upload/v1633459954/usericon_hpewnq.png')
    is_cdc = models.BooleanField('Is cdc', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)
    status = models.BooleanField(default=True)


class Academic(models.Model):
    # Need For Student Tracker Only
    Student = models.PositiveIntegerField(null=True, blank=True)
    Teacher = models.PositiveIntegerField(null=True, blank=True)
    studentenrollment = models.CharField(max_length=100)
    studentdept = models.CharField(
        max_length=40, choices=DeptChoice, default='Computer Science')
    studentyear = models.CharField(
        max_length=40, choices=YearChoice, default='First Year')
    studentsemester = models.CharField(
        max_length=40, choices=SemChoice, default='First Semester')
    subject = models.CharField(
        max_length=80, choices=SubjectChoice, default='Mathematics')
    subjectattendence = models.CharField(max_length=10, null=True, blank=True)
    subjectclass = models.CharField(max_length=10, null=True, blank=True)
    subjectscore = models.CharField(max_length=10, null=True, blank=True)
    subjectmarks = models.CharField(max_length=10, null=True, blank=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)


class Activity(models.Model):
    # Need For Student Tracker Only
    activityname = models.CharField(max_length=70)
    activitydetails = RichTextField(null=True, blank=True)
    activitydate = models.DateField(
        auto_now_add=False, auto_now=False, null=True, blank=True)
    activityowner = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)
