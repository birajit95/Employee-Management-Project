from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Designation, Employee
from Nkrafterz.db_settings import get_connection



def employee_create_view(request):
    connection = get_connection()
    cursor = connection.cursor()

    department_query = """
        SELECT id, department_name FROM employee_management_app_department
        """
    
    cursor.execute(department_query)
    departments = cursor.fetchall()

    departments = [{"id":department[0], "name": department[1]} for department in departments]

  
    designations_query ="""
        SELECT id, designation_name FROM employee_management_app_designation
        """
    cursor.execute(designations_query)
    designations = cursor.fetchall()

    designations = [{"id":designation[0], "name": designation[1]} for designation in designations]
    

    manager_query = """
        SELECT emp.id, emp.first_name || " " || emp.last_name as name FROM employee_management_app_employee emp inner join employee_management_app_designation des
        on emp.designation_id = des.id where des.designation_name = "Manager"
        """
    cursor.execute(manager_query)
    managers = cursor.fetchall()

    managers = [{"id":manager[0], "name": manager[1]} for manager in managers]
    
    cursor.close()
    connection.close()
    
    
    context = {
        "departments": departments,
        "designations": designations,
        "managers": managers
    }
    
    
    return render(request, 'employee_create_template.html', context = context)




def employee_list_view(request):
    connection = get_connection()
    cursor = connection.cursor()

    department_query = """
        SELECT id, department_name FROM employee_management_app_department
        """
    
    cursor.execute(department_query)
    departments = cursor.fetchall()

    departments = [{"id":department[0], "name": department[1]} for department in departments]

  
    designations_query ="""
        SELECT id, designation_name FROM employee_management_app_designation
        """
    cursor.execute(designations_query)
    designations = cursor.fetchall()

    designations = [{"id":designation[0], "name": designation[1]} for designation in designations]
    
    cursor.close()
    connection.close()

    context = {
        "designations": designations,
        "departments": departments
    }

    return render(request, "employee_list_view.html", context=context)



def employee_details_view(request, id):
    context = {'id': id}
    return render(request, "employee_details_view.html", context=context)