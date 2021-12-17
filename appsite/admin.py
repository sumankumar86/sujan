from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'email', 'dept', 'year', 'semester',
                    'enrollment', 'profilepic',
                    'is_cdc', 'is_teacher', 'is_student', 'status']


@admin.register(Academic)
class AcademicAdmin(admin.ModelAdmin):
    list_display = ['id', 'Student', 'Teacher', 'studentenrollment', 'studentdept',
                    'studentyear', 'studentsemester', 'subject', 'subjectattendence', 'subjectclass', 'subjectscore', 'subjectmarks', 'date']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'activityname', 'activitydetails', 'activitydate',
                    'activityowner', 'status']
