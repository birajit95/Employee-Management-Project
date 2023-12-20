from rest_framework import serializers
from pathlib import Path
from django.core.exceptions import ValidationError
from Nkrafterz.db_settings import get_connection
import sqlite3
from generics.utils import generic_file_type_allowance_validation


class EmployeeCreateSerializers(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    contact = serializers.CharField()
    address = serializers.CharField()
    department = serializers.IntegerField()
    designation = serializers.IntegerField()
    manager = serializers.IntegerField()
    joining_date = serializers.DateField()
    id_proof = serializers.FileField()


    def validate(self, data):
        super().validate(data)

        connection = get_connection()
        cursor = connection.cursor()

        designation_name = "Manager"
        emp_id = data.get("designation", 0)
        manager_query =f"""
            SELECT emp.id FROM employee_management_app_employee emp inner join employee_management_app_designation des
            on emp.designation_id = des.id where des.designation_name = "{designation_name}" and emp.id = {emp_id}
            """
        connection.execute(manager_query)
        cursor.execute(manager_query)
        manager = cursor.fetchone()

        if not manager:
            raise ValidationError("Manager not found with this employee id")
        
        department_id = data.get("department", 0)
        department_query = f"""
            SELECT id from employee_management_app_department where id = {department_id}
        """

        cursor.execute(department_query)
        department = cursor.fetchone()
        if not department:
            raise ValidationError("Department not found with this department id")
        

        designation_id = data.get("designation", 0)
        designation_query = f"""
            SELECT id from employee_management_app_designation where id = {designation_id}
        """

        cursor.execute(designation_query)
        designation = cursor.fetchone()
        if not designation:
            raise ValidationError("Designation not found with this designation id")



        

        cursor.close()
        connection.close()


        # only pdf supporting logic
        id_proof = data.get('id_proof')
        if id_proof:
            binary_file = generic_file_type_allowance_validation(id_proof, 'pdf')
            data['id_proof'] = binary_file
        
        return data
        

