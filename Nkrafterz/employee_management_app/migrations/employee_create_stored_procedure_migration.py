from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0011_department_is_active_designation_is_active')
    ]

    operations = [
        migrations.RunSQL('''
            CREATE PROCEDURE insert_employee(
                IN p_first_name VARCHAR(255),
                IN p_last_name VARCHAR(255),
                IN p_email VARCHAR(255),
                IN p_contact VARCHAR(20),
                IN p_address TEXT,
                IN p_department_id INT,
                IN p_designation_id INT,
                IN p_manager_id INT,
                IN p_joining_date DATE,
                IN p_emp_id_proof BLOB,
                IN p_created_at TIMESTAMP
            )
            BEGIN
                INSERT INTO employee_management_app_employee (
                    first_name,
                    last_name,
                    email,
                    contact,
                    address,
                    department_id,
                    designation_id,
                    manager_id,
                    joining_date,
                    emp_id_proof,
                    created_at
                ) VALUES (
                    p_first_name,
                    p_last_name,
                    p_email,
                    p_contact,
                    p_address,
                    p_department_id,
                    p_designation_id,
                    p_manager_id,
                    p_joining_date,
                    p_emp_id_proof,
                    p_created_at
                );
                END;            
        '''),
    ]