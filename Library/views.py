from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Library.models import User, Administrator


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        data = {
            "title": "Register",
        }
        return render(request, 'register.html', context=data)
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        gender_pre = request.POST.get("gender")
        if gender_pre == 'M':
            gender = True
        else:
            gender = False
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        user = User()
        user.user_name = username
        user.user_password = password
        user.user_name = name
        user.user_gender = gender
        user.user_age = age
        user.user_phone = phone
        # user.save()
        print(gender)
        return redirect(reverse("library:login"))


def login(request):
    if request.method == "GET":
        data = {
            "title": "Register",
        }
        return render(request, 'login.html', context=data)
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_exist = User.objects.filter(user_name=username).count()
        admin_exist = Administrator.objects.filter(admin_username=username).count()
        if user_exist + admin_exist:
            return HttpResponse('User not exist')
        elif user_exist:
            user = User.objects.filter(user_name=username)
            if password == user.user_password:
                return redirect(reverse('library:user_index'))
            else:
                return HttpResponse('Invalid password or username')
        else:
            administrator = Administrator.objects.filter(user_name=username)
            if password == administrator.admin_password:
                return redirect(reverse('library:admin_index'))
            else:
                return HttpResponse('Invalid password or username')


def user_index(request):
    return HttpResponse('Welcome User!')


def admin_index(request):
    return HttpResponse('Welcome Admin!')
