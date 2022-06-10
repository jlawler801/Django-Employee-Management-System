from tkinter import Widget
from warnings import filters
import django_filters
from django_filters import DateFilter, CharFilter
from django.forms import TextInput

from .models import *

class EmployeeFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(label='Name' ,field_name='emp__name', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': 'Name', 'class': 'search'}))
    class Meta:
        model = EmpDept
        fields = ['Name']
        