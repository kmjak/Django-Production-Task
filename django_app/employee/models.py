from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department_name = models.CharField(max_length=10)

class Employee(models.Model):
    employee_id = models.CharField(max_length=6, primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name