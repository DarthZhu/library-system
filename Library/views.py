from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Library.models import User, Administrator, Book, AdminBill, UserBill


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
        # print(gender)
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


def admin_index(request, id):
    data = {
        "id": id,
    }
    return render(request, 'admin_index.html', context=data)


def admin_search(request, id):
    books = Book.objects.all()
    if request.method == "GET":
        data = {
            "title": "search",
            "id": id,
            "books": books,
        }
        return render(request, 'admin_search.html', context=data)
    else:
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('isbn')
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


def admin_add(request, id):
    if request.method == "GET":
        data = {
            "title": "Add",
            "id": id,
        }
        return render(request, 'admin_add.html', context=data)
    else:
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        price_sold = request.POST.get('price_sold')
        price_sold = int(price_sold)
        price_bought = request.POST.get('price_bought')
        price_bought = int(price_bought)
        amount = request.POST.get('amount')
        amount = int(amount)
        book = Book.objects.filter(bookname=book_name).filter(ISBN=isbn)
        book = book.filter(author=author).filter(publisher=publisher)
        # print(book.count())
        if book.count() == 0:
            # print('Not exist')
            book = Book()
            book.bookname = book_name
            book.ISBN = isbn
            book.author = author
            book.publisher = publisher
            book.price = price_sold
            # book.save()
        else:
            book = list(book)
            book = book[0]
        bill = AdminBill()
        admin = Administrator.objects.filter(id=id)
        admin = list(admin)
        admin = admin[0]
        bill.adminID = admin
        bill.price = price_bought
        bill.amount = amount
        bill.book = book
        # bill.save()
        return HttpResponse('Purchase Success')


def admin_edit(request, id):
    if request.method == "GET":
        data = {
            "title": "Edit",
            "id": id,
        }
        return render(request, 'admin_edit.html', context=data)
    else:
        b_id = request.POST.get('book_id')
        book = Book.objects.filter(id=b_id)
        if book.count() == 0:
            return HttpResponse('Book not exist')
        else:
            book = list(book)
            book = book[0]
            book_name = request.POST.get('book_name')
            isbn = request.POST.get('isbn')
            author = request.POST.get('author')
            publisher = request.POST.get('publisher')
            price_sold = request.POST.get('price_sold')
            amount = request.POST.get('amount')
            if book_name != "":
                book.bookname = book_name
            if isbn != "":
                book.ISBN = isbn
            if author != "":
                book.author = author
            if publisher != "":
                book.publisher = publisher
            if price_sold != "":
                price_sold = int(price_sold)
                book.price = price_sold
            if amount != "":
                amount = int(amount)
                book.amount = amount
            # book.save()
            # print(book.author)
            return HttpResponse('Edit Succeed')


def admin_bill(request, id):
    bills = AdminBill.objects.filter(adminID=id)
    data = {
        "title": "Register",
        "id": id,
        "bills": bills,
    }
    return render(request, 'admin_bill.html', context=data)


def admin_pay(request, id):
    bills = AdminBill.objects.filter(adminID=id).filter(is_cancelled=False).filter(is_pay=False)
    if bills.count() == 0:
        return HttpResponse('No bill needs to be paid')
    if request.method == "GET":
        data = {
            "title": "Pay",
            "id": id,
            "bills": bills,
        }
        return render(request, 'admin_pay.html', context=data)
    else:
        bill_id = request.POST.get('bill_id')
        bill_id = int(bill_id)
        bill = bills.filter(id=bill_id)
        if bill.count() == 0:
            return HttpResponse('Bill is invalid, cancelled or already paid')
        else:
            bill = list(bill)
            bill = bill[0]
            bill.is_pay = True
            # bill.save()
            return HttpResponse('Bill is paid')


def admin_confirm(request, id):
    bills = AdminBill.objects.filter(adminID=id).filter(is_cancelled=False).filter(is_pay=True).filter(is_sent=False)
    if bills.count() == 0:
        return HttpResponse('No order needs to be confirmed')
    if request.method == "GET":
        data = {
            "title": "Pay",
            "id": id,
            "bills": bills,
        }
        return render(request, 'admin_confirm.html', context=data)
    else:
        bill_id = request.POST.get('bill_id')
        bill_id = int(bill_id)
        bill = bills.filter(id=bill_id)
        if bill.count() == 0:
            return HttpResponse('Bill is invalid, cancelled or is not paid')
        else:
            bill = list(bill)
            bill = bill[0]
            bill.is_sent = True
            book = bill.book
            # print(book.amount)
            book.amount += bill.amount
            # print(book.amount)
            # book.save()
            # bill.save()
            return HttpResponse('Order is received')


def admin_cancel(request, id):
    bills = AdminBill.objects.filter(adminID=id).filter(is_cancelled=False).filter(is_pay=False)
    if bills.count() == 0:
        return HttpResponse('No bill can be cancelled')
    if request.method == "GET":
        data = {
            "title": "Pay",
            "id": id,
            "bills": bills,
        }
        return render(request, 'admin_cancel.html', context=data)
    else:
        bill_id = request.POST.get('bill_id')
        bill_id = int(bill_id)
        bill = bills.filter(id=bill_id)
        if bill.count() == 0:
            return HttpResponse('Bill is invalid, cancelled ,is paid or is received')
        else:
            bill = list(bill)
            bill = bill[0]
            bill.is_pay = False
            bill.is_sent = False
            bill.is_cancelled = True
            # bill.save()
            return HttpResponse('Order has been cancelled')


def user_index(request, id):
    data = {
        "id": id,
    }
    return render(request, 'user_index.html', context=data)


def user_search(request, id):
    books = Book.objects.all()
    if request.method == "GET":
        data = {
            "title": "search",
            "id": id,
            "books": books,
        }
        return render(request, 'user_search.html', context=data)
    else:
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('isbn')
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
        return render(request, 'user_search.html', context=data)


def user_bill(request, id):
    bills = UserBill.objects.filter(userID=id)
    data = {
        "title": "Register",
        "id": id,
        "bills": bills,
    }
    return render(request, 'admin_bill.html', context=data)


def user_buy(request, id):
    books = Book.objects.all()
    if request.method == "GET":
        data = {
            "title": "Add",
            "id": id,
            "books": books,
        }
        return render(request, 'user_buy.html', context=data)
    else:
        book_name = request.POST.get('book_name')
        isbn = request.POST.get('isbn')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        amount = request.POST.get('amount')
        if book_name:
            book = books.filter(bookname=book_name)
        if isbn:
            book = book.filter(ISBN=isbn)
        if author:
            book = book.filter(author=author)
        if publisher:
            book = book.filter(publisher=publisher)
        if amount == "":
            return HttpResponse('Please input the amount you want to buy')
        amount = int(amount)
        if book.count() == 0:
            return HttpResponse('Book not exist')
        elif book.count() > 1:
            return HttpResponse('Too few descriptions')
        else:
            book = list(book)
            book = book[0]
            if book.amount == 0:
                return HttpResponse('Out of Stock')
            else:
                if amount > book.amount:
                    return HttpResponse('Not enough book')
                else:
                    bill = UserBill()
                    user = User.objects.filter(id=id)
                    user = list(user)
                    user = user[0]
                    bill.userID = user
                    bill.amount = amount
                    bill.book = book
                    bill.pay = amount * book.price
                    book.amount -= amount
                    # print(bill.pay)
                    # print(book.amount)
                    # bill.save()
                    # book.save()
                    return HttpResponse('Purchase Success')


def user_pay(request, id):
    bills = UserBill.objects.filter(userID=id).filter(is_cancelled=False).filter(is_pay=False)
    if bills.count() == 0:
        return HttpResponse('No bill needs to be paid')
    if request.method == "GET":
        data = {
            "title": "Pay",
            "id": id,
            "bills": bills,
        }
        return render(request, 'user_pay.html', context=data)
    else:
        bill_id = request.POST.get('bill_id')
        bill_id = int(bill_id)
        bill = bills.filter(id=bill_id)
        if bill.count() == 0:
            return HttpResponse('Bill is invalid, cancelled or already paid')
        else:
            bill = list(bill)
            bill = bill[0]
            bill.is_pay = True
            # bill.save()
            return HttpResponse('Bill is paid')


def user_confirm(request, id):
    bills = UserBill.objects.filter(userID=id).filter(is_cancelled=False).filter(is_pay=True).filter(is_sent=False)
    if bills.count() == 0:
        return HttpResponse('No order needs to be confirmed')
    if request.method == "GET":
        data = {
            "title": "Pay",
            "id": id,
            "bills": bills,
        }
        return render(request, 'admin_confirm.html', context=data)
    else:
        bill_id = request.POST.get('bill_id')
        bill_id = int(bill_id)
        bill = bills.filter(id=bill_id)
        if bill.count() == 0:
            return HttpResponse('Bill is invalid, cancelled or is not paid')
        else:
            bill = list(bill)
            bill = bill[0]
            bill.is_sent = True
            # bill.save()
            return HttpResponse('Order is received')

