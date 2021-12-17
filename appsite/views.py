from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from .decorator import *
from django.core.exceptions import PermissionDenied
from datetime import datetime
from datetime import date

# Create your views here.


@OnlyAuth
def signin(request):
    LM = LoginForm(request.POST or None)
    if request.method == 'POST':
        if LM.is_valid():
            UserName = request.POST.get('username')
            PassWord = request.POST.get('password')
            user = authenticate(request, username=UserName, password=PassWord)

            if user is not None and user.is_cdc:
                login(request, user)
                return redirect('cdc')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('TeacherProfile')
            elif user is not None and user.is_student:
                login(request, user)
                return redirect('StudentProfile')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, LM.errors)
    else:
        LM = LoginForm()
    context = {'form': LM}
    return render(request, 'common/signin.html', context)


@OnlyAuth
def signup(request):
    if request.method == 'POST':
        SF = SignupForm(request.POST)
        if SF.is_valid():
            isStudent = SF.cleaned_data.get('is_student')
            isTeacher = SF.cleaned_data.get('is_teacher')
            if isStudent:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_student = True
                SignUpUser.status = True
                SignUpUser.save()
            elif isTeacher:
                SignUpUser = SF.save(commit=False)
                SignUpUser.is_teacher = True
                SignUpUser.status = False
                SignUpUser.save()
            else:
                messages.warning(request, 'Please Select Your user Type')
                return redirect('signin')
            user = SF.cleaned_data.get('username')
            messages.success(request, 'Account Created for ' + user)
            return redirect('signin')
        else:
            messages.error(request, SF.errors)
    else:
        SF = SignupForm()
    context = {'form': SF}
    return render(request, 'common/signup.html',context)


@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')


def contactus(request):
    return render(request, 'common/contactus.html')


def StudentProfile(request):
    return render(request, 'site/StudentProfile.html')


def TeacherProfile(request):
    return render(request, 'site/TeacherProfile.html')


def StudentSearch(request):
    return render(request, 'site/StudentSearch.html')


def StudentView(request):
    return render(request, 'site/StudentView.html')


def StudentMarks(request):
    return render(request, 'site/StudentMarks.html')



def semester(request):
    return render(request, 'site/semester.html')


def attendance(request):
    return render(request, 'site/attendance.html')





@login_required(login_url='signin')
def editProfile(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_student = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'site/editProfile.html', context)

@login_required(login_url='signin')
def studentactivity(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    Activitydata = Activity.objects.filter(activityowner=request.user.id)
    if request.method == 'POST':
        ActivityProfileForm = ActivityProfile(request.POST, request.FILES)
        if ActivityProfileForm.is_valid():
            studentActivity = ActivityProfileForm.save(commit=False)
            studentActivity.status = False
            studentActivity.activityowner = request.user.id
            studentActivity.save()
            messages.success(
                request, 'Your Activity Details is submited and wait for CDC process')
            return redirect('studentactivity')
        else:
            messages.warning(request, ActivityProfileForm.errors)
    else:
        ActivityProfileForm = ActivityProfile()

    context = {'StudentData': userdata, 'Activitydata': Activitydata,
               'ActivityProfileForm': ActivityProfileForm}
    return render(request, 'site/studentactivity.html', context)


@login_required(login_url='signin')
def academic(request):
    return render(request, 'site/studentactivity.html')


@login_required(login_url='signin')
def teacher(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    return render(request, 'site/TeacherProfile.html')


# @login_required(login_url='signin')
# def cdc(request):
#     if not request.user.is_cdc:
#         raise PermissionDenied
#     return render(request, 'admin/CdcProfile.html')


@login_required(login_url='signin')
def TeacherProfile(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        UserProfileForm = SignupForm(
            request.POST, request.FILES, instance=userdata)

        if UserProfileForm.is_valid():
            student = UserProfileForm.save(commit=False)
            student.is_teacher = True
            student.status = True
            UserProfileForm.save()
            messages.success(
                request, 'Profile is Updated. please login again to craete a new Session')
            return redirect('signout')
        else:
            messages.warning(request, UserProfileForm.errors)
    else:
        UserProfileForm = SignupForm(instance=userdata)
    context = {'StudentData': userdata, 'UserProfileForm': UserProfileForm}
    return render(request, 'site/TeacherProfile.html', context)


def allstudent(request):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')

    userdata = User.objects.get(pk=request.user.id)
    studentdata = User.objects.all()
    allstudent = []

    for i in studentdata:
        if i.is_student == True:
            allstudent.append({
                "id": i.id,
                "first_name": i.first_name,
                "last_name": i.last_name,
                'dept': i.dept,
                'year': i.year,
                'semester': i.semester,
                'enrollment': i.enrollment,
                'profilepic': i.profilepic,
            })

    context = {'StudentData': userdata, 'allstudent': allstudent}
    return render(request, 'site/allstudent.html', context)

#for teacher only


def addacademic(request, pk):
    if not request.user.is_teacher:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    studentdetails = User.objects.get(pk=pk)
    StudentMarks = Academic.objects.filter(Student=pk)

    if request.method == 'POST':
        AcademicForm = AcademicProfile(request.POST)
        if AcademicForm.is_valid():
            AcademicUser = AcademicForm.save(commit=False)
            AcademicUser.Student = pk
            AcademicUser.Teacher = request.user.id
            AcademicUser.studentenrollment = studentdetails.enrollment
            AcademicUser.date = date.today()
            AcademicUser.save()
            messages.success(
                request, 'Marks & Attendence is Saved')
            return redirect('allstudent')
        else:
            messages.warning(request, AcademicForm.errors)
    else:
        AcademicForm = AcademicProfile()
    context = {'StudentData': userdata, 'AcademicForm': AcademicForm,
               'studentdetails': studentdetails, 'StudentMarks': StudentMarks}
    return render(request, 'site/Academic.html', context)

#for student only


def StudentProfile(request):
    if not request.user.is_student:
        raise PermissionDenied
    if not request.user.status:
        return render(request, 'common/notActive.html')
    userdata = User.objects.get(pk=request.user.id)
    StudentMarks = Academic.objects.filter(Student=request.user.id)
    context = {'StudentData': userdata, 'StudentMarks': StudentMarks}
    return render(request, 'site/StudentProfile.html', context)
