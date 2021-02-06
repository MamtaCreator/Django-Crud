from django import forms

from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
         model=Employee
         #fields='__all__'  #geting all the fields from models
         fields =('fullname','mobile','emp_code','position')

         labels = {
             'fullname':'Full Name',
             'mobile':'Mobile number',
             'emp_code':'Employee Code',
             'position':'Position'

         }
#to change ----- inside the  position field into select
    def __init__(self ,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs) #contructor
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required =False     
