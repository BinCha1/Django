from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee


# Create your views here.
def employee_detail(request,pk):
    employee=get_object_or_404(Employee, pk=pk)
    return HttpResponse(employee)