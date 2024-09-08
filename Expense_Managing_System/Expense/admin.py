from django.contrib import admin
from .models import BankAccount, Expenses
# Register your models here.

admin.site.register(BankAccount)
admin.site.register(Expenses)