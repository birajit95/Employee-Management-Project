***=======================Employee Management APP==========================***

This is a simple employe management software to manage employees data.

<br/>
<br/>
<br/>

key skills used:
1. python 3.11
2. django
3. django rest framework
4. jinja 2
5. HTML
6. JavaScript
7. BootStrap
8. sqlite3


<br/>

**Steps to start the project:**
1. create virtual env using the following command:

`python3.11 -m venv env`

2. Then activate it from the same directory where it is created using 

`source env/bin/activate`

3. Now run the following command to install all the dependacies in the virtual environment

`pip install -r requirements.txt`

4. run the following commands to migrate the models in the database

`python manange.py makemigrations` and
`python manage.py migrate`

5. Now to start the server, run the following command,

`python manage.py runserver`

6. Now open the web-browser and goto http://localhost:8000/emp_app/emp-create-form/



<br/>
<br/>
<br/>



**NOTE*:
1. >As all the queries are written in raw sql form so I only used APIView of drf instead of the generic views like CreateAPIVIew, ListAPIVIew, RetrieveUpdateDeleteAPIView etc.

2. >As sqlite3 does not support stored procedure so I used direct raw sql queries in the api and views. 

3. >But I have created migration file containing the stored procedure creation sql script to migrate to the database. The file name is 'employee_create_stored_procedure_migration.py' inside the migrations dir of employee_management_app app

3. >I have not used any auth system to keep it simple 






