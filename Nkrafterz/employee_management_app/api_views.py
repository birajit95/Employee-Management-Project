from generics.utils import get_current_financial_year
from .models import Department, Designation, Employee
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import EmployeeCreateSerializers
from Nkrafterz.db_settings import get_connection
from django.utils import timezone
from datetime import datetime
from django.db import DatabaseError


class EmployeeCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = EmployeeCreateSerializers(data=data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        values = data.values()

        is_error = False

        try:

            connection = get_connection()
            cursor = connection.cursor()

            insert_query = f"""
            INSERT INTO employee_management_app_employee (first_name, last_name, email, contact, address, department_id, designation_id, manager_id, joining_date, emp_id_proof, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?);
            """
            values_list = list(values)
            values_list.append(timezone.now())
            values = tuple(values_list)

            cursor.execute(insert_query, values)
            connection.commit()

            cursor.close()
            connection.close()

        except DatabaseError as e:
            print("data base error:", e)
            is_error = True
        
        except Exception as e:
            print(e)
            is_error = True

        status_code = 200
        message = "data saved successfully"

        if is_error:
            status_code = 500
            message = "Internal Server Error"
            
        response = {
            "status_code": status_code,
            "message": message
        }

        return Response(response)
    


class EmpployeeListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        department_id = request.GET.get('department_id')
        designation_id = request.GET.get('designation_id')


        connection = get_connection()
        cursor = connection.cursor()

        employe_query = """
            SELECT emp.id, emp.first_name, emp.last_name, emp.email, emp.contact, dep.department_name, des.designation_name, man.first_name || " " || man.last_name as manager_name 
            FROM employee_management_app_employee emp INNER JOIN employee_management_app_department dep ON emp.department_id = dep.id
            INNER JOIN employee_management_app_designation des ON emp.designation_id = des.id 
            LEFT JOIN employee_management_app_employee man ON emp.manager_id = man.id
        """

        if search or designation_id or department_id:
            employe_query += " WHERE "

        if search:
            employe_query += f""" 
            emp.first_name LIKE '%{search}%' 
            OR
            emp.last_name LIKE '%{search}%' 
            OR
            emp.email LIKE '%{search}%'
            OR
            emp.contact LIKE '%{search}%'
            OR
            dep.department_name LIKE '%{search}%' 
            OR
            des.designation_name LIKE '%{search}%' 
            """

        if search and (department_id or designation_id):
            employe_query += " AND "

        if department_id:
            employe_query += f"""
            emp.department_id = {department_id}
            """

        # if (designation_id and department_id):
        #     employe_query += " AND "

        # if designation_id:
        #     employe_query += f"""
        #     emp.designation_id = {designation_id}
        #     """

        # print(employe_query)

        cursor.execute(employe_query)

        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        

        cursor.close()
        connection.close()
        response = {
            "status_code": 200,
            "message": "data fetched successfully",
            "data": result,
            "total_items": len(result)
        }

        return Response(response, status=200)



class EmployeeDetailsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        connection = get_connection()
        cursor = connection.cursor()
        
        current_financial_year = get_current_financial_year()


        employe_query = f"""
                SELECT emp.id, emp.first_name, emp.last_name, emp.email, emp.contact, dep.department_name, des.designation_name, emp.joining_date,
                man.first_name || " " || man.last_name as manager_name, sal.net_amount, sal.gross_amount, sal.deduction 
                FROM employee_management_app_employee emp INNER JOIN employee_management_app_department dep ON emp.department_id = dep.id
                INNER JOIN employee_management_app_designation des ON emp.designation_id = des.id 
                LEFT JOIN employee_management_app_employee man ON emp.manager_id = man.id
                LEFT JOIN employee_management_app_salary sal ON emp.id = sal.employee_id AND sal.financial_year={current_financial_year}
                WHERE emp.id = {id}
            """
        
        cursor.execute(employe_query)
        columns = [column[0] for column in cursor.description]
        employe_data_result = [dict(zip(columns, row)) for row in cursor.fetchall()]


        task_tracking_query = f"""
                SELECT t.id, tt.task_id, t.task_name, tt.progress_percent, tt.created_at,

                CASE
                    WHEN tt.is_completed = true THEN 'Completed'
                    WHEN tt.progress_percent > 0 THEN 'In progress'
                    ELSE 'Pending'
                END AS task_status
                FROM tasks_app_tasktracker tt
                INNER JOIN
                tasks_app_task t
                ON
                tt.task_id = t.id
                INNER JOIN
                employee_management_app_employee e
                ON
                tt.employee_id = e.id
                WHERE
                e.id = {id}
        """
        cursor.execute(task_tracking_query)
        columns = [column[0] for column in cursor.description]
        tasks_result = [dict(zip(columns, row)) for row in cursor.fetchall()]


        transactions_query = f"""
                SELECT t.id, t.transaction_id, t.transaction_amount, t.created_at
                FROM transaction_app_transactions t
                INNER JOIN
                employee_management_app_employee e
                ON
                t.employee_id = e.id
                WHERE
                e.id = {id}
        """
        cursor.execute(transactions_query)
        columns = [column[0] for column in cursor.description]
        transaction_data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        

        cursor.close()
        connection.close()

        data = {
            "employee_data": employe_data_result[0] if employe_data_result else {},
            "task_record": tasks_result[0] if tasks_result else {},
            'transaction_record': transaction_data[0] if transaction_data else {}
        }

        response = {
            "status_code": 200,
            "data": data
        }

        return Response(response)

        






