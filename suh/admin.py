from unicodedata import name
from django.contrib import admin
from .models import EmpDept, Roles, Employee

# Register your models here.
admin.site.register(EmpDept)
admin.site.register(Roles)
admin.site.register(Employee)