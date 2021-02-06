from django.shortcuts import render ,redirect
from .models import Employee

from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    #fetch records

    context ={'employee_list':Employee.objects.all()}
    return render (request, "employee_register/employee_list.html",context)

def employee_form(request,id=0):
    
    if request.method=='GET':
        if id==0: #insert
            form = EmployeeForm() #instance of  class EmployeeForm from form.py file 
        else: #update
            employee = Employee.objects.get(pk=id)    
            form = EmployeeForm( instance=employee)
        return render (request, "employee_register/employee_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST) 
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,  instance=employee)    
        if form.is_valid():
            form.save()  
        return redirect('/employee/list')     

def employee_delete(request,id):
    employeeToDelete= Employee.objects.get(pk=id)
    employeeToDelete.delete()
    return redirect('/employee/list')
