from django.db import models
from employee_management_app.models import Employee
from generics.abstract_models import TimeStampModel

class Transactions(TimeStampModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=300)
