from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.employee_form,name='employee_insert'), #get and post request to insert ops
    path('<int:id>/', views.employee_form,name="employee_update"), #get and post request to update ops
    path('delete/<int:id>',views.employee_delete,name="employee_delete"),
    path('list/', views.employee_list,name='employee_list') #get request to fetch ops
]
