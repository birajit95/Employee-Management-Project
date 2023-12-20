from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('emp-create-form/', views.employee_create_view, name='emp_create_view'),
    path('emp-list-view/', views.employee_list_view, name='emp_list_view'),
    path('emp-details-view/<int:id>', views.employee_details_view, name='emp_details_view'),


] + [
    path('emp-create/', api_views.EmployeeCreateAPIView.as_view(), name='emp_create_api'),
    path('emp-list/', api_views.EmpployeeListAPIView.as_view(), name='emp_list_api'),
    path('emp-details/<int:id>', api_views.EmployeeDetailsAPIView.as_view(), name='emp_details_api'),



]
