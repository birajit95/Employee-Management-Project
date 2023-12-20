from django.db import models
from generics.abstract_models import TimeStampModel

class Department(TimeStampModel):
    department_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)


class Designation(models.Model):
    designation_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class Employee(TimeStampModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    joining_date = models.DateField()
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name='designation_emp_set')
    # emp_id_proof = models.FileField(upload_to='media/emp_id_proofs/', null=True, blank=True)
    emp_id_proof = models.BinaryField(null=True, blank=True)
    contact = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email_constraint'),
            models.UniqueConstraint(fields=['contact'], name='unique_contact_constraint'),
        ]



class Salary(TimeStampModel):
    """
    This is just to hold the salary info if an employee,
    Salary Transaction record model is in transaction_app
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deduction = models.DecimalField(max_digits=10, decimal_places=2)
    financial_year = models.CharField(max_length=250)
