from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department_name = models.CharField(max_length=10)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id = models.CharField(max_length=6, primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name


    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

        if self.department.department_name == 'Sales':
            Sales.objects.create(department=self.department, employee=self)
        elif self.department.department_name == 'Personnel':
            Personnel.objects.create(department=self.department, employee=self)
        elif self.department.department_name == 'Production':
            Production.objects.create(department=self.department, employee=self)
        elif self.department.department_name == 'Product':
            Product.objects.create(department=self.department, employee=self)


class Sales(models.Model):
    order_information = models.BooleanField(default=True)
    customer_information = models.BooleanField(default=True)
    product_information = models.BooleanField(default=True)
    stock_information = models.BooleanField(default=True)
    order_aggregate = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sales Access for {self.employee.employee_name}"


class Personnel(models.Model):
    employee_information = models.BooleanField(default=True)
    division_information = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Personnel Access for {self.employee.employee_name}"


class Production(models.Model):
    production_information = models.BooleanField(default=True)
    inventory_management_product = models.BooleanField(default=True)
    arrival_management_product = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Production Access for {self.employee.employee_name}"


class Product(models.Model):
    product_information = models.BooleanField(default=True)
    inventory_information = models.BooleanField(default=True)
    shipping_information = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Product Access for {self.employee.employee_name}"
