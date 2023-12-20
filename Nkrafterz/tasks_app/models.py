from django.db import models
from employee_management_app.models import Employee
from generics.abstract_models import TimeStampModel

class Task(TimeStampModel):
    task_name = models.CharField(max_length=100)
    descriptions = models.TextField(null=True, blank=True)

class TaskTracker(TimeStampModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=True)
    progress_percent = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.is_completed:
            self.progress_percent = 100.0
            self.save()

        return super(TaskTracker, self).save(*args, **kwargs)



