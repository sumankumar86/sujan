from django.contrib import admin
from django.urls import path
from appsite import views
admin.site.site_header = "CDC ADMIN"
admin.site.site_title = "CDC ADMIN"
admin.site.index_title = "CDC ADMIN"


urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('contactus/', views.contactus, name='contactus'),
    path('StudentProfile/', views.StudentProfile, name='StudentProfile'),
    path('TeacherProfile/', views.TeacherProfile, name='TeacherProfile'),
    path('StudentSearch/', views.StudentSearch, name='StudentSearch'),
    path('StudentView/', views.StudentView, name='StudentView'),
    path('StudentMarks/', views.StudentMarks, name='StudentMarks'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('studentactivity/', views.studentactivity, name='studentactivity'),
    path('semester/', views.semester, name='semester'),
    path('attendance/', views.attendance, name='attendance'),
    path('allstudent/', views.allstudent, name='allstudent'),
    path('addacademic/<int:pk>', views.addacademic, name='addacademic'),
    # path('viewacademic', views.viewacademic, name='viewacademic'),

]
