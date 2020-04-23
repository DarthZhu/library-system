from django.contrib import admin
from .models import Book, Administrator, User, AdminBill, UserBill
# Register your models here.
admin.site.register(Book)
admin.site.register(Administrator)
admin.site.register(User)
admin.site.register(AdminBill)
admin.site.register(UserBill)
