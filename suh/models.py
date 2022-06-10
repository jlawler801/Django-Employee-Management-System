from django.db import models
from django.urls import reverse

class Deptartments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    departments = models.CharField(db_column='Departments', max_length=30, blank=True, null=True)  # Field name made lowercase.
    manager = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Manager_ID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.departments

    class Meta:
        managed = False
        db_table = 'deptartments'


class EmpDept(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emp = models.ForeignKey('Employee', models.DO_NOTHING, db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Deptartments, models.DO_NOTHING, db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Role_ID', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.emp.name

    class Meta:
        managed = False
        db_table = 'emp_dept'


class Employee(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def get_absolute_url(self):
        return reverse("beep", kwargs={"id": self.id})

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'employee'


class Roles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.role

    class Meta:
        managed = False
        db_table = 'roles'

        

