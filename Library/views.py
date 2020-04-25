from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Library.models import User, Administrator, Book


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
        # print(username)
        # print(password)
        user_exist = User.objects.filter(user_username=username).count()
        admin_exist = Administrator.objects.filter(admin_username=username).count()
        # print(user_exist)
        # print(admin_exist)
        if user_exist + admin_exist == 0:
            return HttpResponse('User not exist')
        elif user_exist:
            user = User.objects.filter(user_username=username)
            user = list(user)
            user = user[0]
            if password == user.user_password:
                return redirect(reverse('library:user_index', kwargs={'id': user.id}))
            else:
                return HttpResponse('Invalid password or username')
        else:
            administrator = Administrator.objects.filter(admin_username=username)
            administrator = list(administrator)
            administrator = administrator[0]
            if password == administrator.admin_password:
                return redirect(reverse('library:admin_index', kwargs={'id': administrator.id}))
            else:
                return HttpResponse('Invalid password or username')


def user_index(request, id):
    return HttpResponse('Welcome User!')


def admin_index(request, id):
    data = {
        "id": id,
    }
    return render(request, 'admin_index.html', context=data)


def admin_booklist(request, id):
    books = Book.objects.all()
    data = {
        "books": books,
        "id": id,
    }
    return render(request, 'booklist.html', context=data)


def admin_search(request, id):
    if request.method == "GET":
        data = {
            "title": "search",
            "id": id,
        }
        return render(request, 'admin_search.html', context=data)
    else:
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('ISBN')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        result = Book.objects.all()
        if book_name:
            result = result.filter(bookname=book_name)
        if isbn:
            result = result.filter(ISBN=isbn)
        if author:
            result = result.filter(author=author)
        if publisher:
            result = result.filter(publisher=publisher)
        data = {
            "books": result,
            "id": id,
        }
        return render(request, 'admin_search.html', context=data)
