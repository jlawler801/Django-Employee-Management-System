
from django import forms
from .models import Employee, Deptartments, Roles, EmpDept



class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmpEmpform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name']

class EmpDeptform(forms.ModelForm):
    class Meta:
        model = Deptartments
        fields = ['departments']

class EmpRolesform(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'

class EmployeeDeptform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['emp'].required = True
        self.fields['dept'].required = True
        self.fields['role'].required = True
        self.fields['salary'].required = True
    class Meta:
        model = EmpDept
        fields = '__all__'
        widgets = {
            'start_date': forms.TextInput(attrs={'id': 'datepicker'}),
        }
