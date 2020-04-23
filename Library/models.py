from django.db import models


class Book(models.Model):
    ISBN = models.IntegerField()
    bookname = models.CharField(max_length=16)
    author = models.CharField(max_length=16, null=True)
    publisher = models.CharField(max_length=16, null=True)
    price = models.IntegerField(null=False, default=0)
    amount = models.IntegerField(null=False, default=0)
    amount_left = models.IntegerField(null=False, default=0)


class Administrator(models.Model):
    admin_username = models.CharField(max_length=16)
    admin_password = models.CharField(max_length=16)
    admin_name = models.CharField(max_length=16)
    admin_gender = models.BooleanField(default=True)  # True = Male, False = Female
    admin_age = models.IntegerField()
    admin_phone = models.CharField(max_length=11)
    is_delete = models.BooleanField(default=False)


class User(models.Model):
    user_username = models.CharField(max_length=16)
    user_password = models.CharField(max_length=16)
    user_name = models.CharField(max_length=16)
    user_gender = models.BooleanField(default=True)  # True = Male, False = Female
    user_age = models.IntegerField()
    user_phone = models.CharField(max_length=11)
    is_delete = models.BooleanField(default=False)


class AdminBill(models.Model):
    adminID = models.ForeignKey('Administrator', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    outcome = models.IntegerField()
    is_pay = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)


class UserBill(models.Model):
    userID = models.ForeignKey('User', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    income = models.IntegerField()
    is_pay = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

