
from email.policy import default
from django.shortcuts import redirect, render
from .models import EmpDept, Employee
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from .forms import EmpDeptform, EmpRolesform, Employeeform, EmployeeDeptform
from .filters import EmployeeFilter
from django.contrib.auth import authenticate, login, logout, get_user_model
import time
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView




def employee_data(request):
    form = Employeeform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'employee.html', context)

@login_required
def kroo_view(request):
    form = EmployeeDeptform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'about.html', context)

def role_view(request):
    form = EmpRolesform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'form': form}
    return render(request, 'role.html', context)

def scroop(request):
    qsvor = EmpDept.objects.select_related('emp', 'dept', 'role').order_by("dept")
    myFilter = EmployeeFilter(request.GET, queryset=qsvor)
    qsvor = myFilter.qs
    if request.htmx:
        return render(request, 'search.html', {'cross': qsvor, 'myFilter': myFilter})
    return render(request, "home.html", {'cross': qsvor, 'myFilter': myFilter})
    

    

def emp_info_view(request, id):

    form = Employee.objects.get(id=id)
    context = {'form': form}
    return render(request, 'employee_data.html', context)

@login_required
def delete_confirm(request, id):
    employee = EmpDept.objects.get(id=id)
    employee.delete()
    employees = EmpDept.objects.all().order_by("dept")
    return render(request, 'home.html', {'cross': employees} )
    

@login_required
def update(request, id):
    employee = EmpDept.objects.get(id=id)
    form = EmployeeDeptform(instance=employee)
    if request.method == 'POST':
        form = EmployeeDeptform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {'form': form}
    return render(request, 'about.html', context)

def login_user1(request):
    if request.method == 'POST':
        form = AuthenticationForm
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            time.sleep(1)
        else:
            return HttpResponseForbidden()
    return render(request, 'loginout/login.html', {})

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<script id='username-success' class='sucess'>document.getElementById('username').style.backgroundColor = 'lightgreen';</script>")
    else:
        return HttpResponse("<script id='username-success' class='sucess'>document.getElementById('username').style.backgroundColor = 'white';</script>")


    







    # def test_base(request):
#     cursor = connection.cursor()
#     cursor.execute("select d.ID, e.Name, de.Departments, r.role, Salary, coalesce (Start_Date, 'TBA') as Start_Date from emp_dept d inner join employee e on d.Emp_ID = e.ID inner join deptartments de on d.Dept_ID = de.ID inner join roles r on d.Role_ID = r.ID order by ID")
#     row = dictfetchall(cursor)
#     return render(request, 'home.html', {'posts': row})
# # Create your views here.

# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]