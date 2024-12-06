from django.db import models

# Create your models here.
class Department(models.Model):
    department_id = models.CharField(max_length=6, primary_key=True)
    department_name = models.CharField(max_length=10)

    def __str__(self):
        return self.department_name

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

class Employee(models.Model):
    employee_id = models.CharField(max_length=6, primary_key=True)
    employee_name = models.CharField(max_length=200)
    employee_password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
    
    def getAccessList(self):
        department = self.department
        access_list = []

        sales_access = Sales.objects.filter(department=department, employee=self.employee_id).first()
        if sales_access:
            if sales_access.order_information:
                access_list.append({"display_name": "受注管理", "goto": "order_management"})
            if sales_access.customer_management:
                access_list.append({"display_name": "得意先情報", "goto": "customer_management"})
            if sales_access.customer_edit:
                access_list.append({"display_name": "得意先編集", "goto": "customer_edit"})
            if sales_access.customer_delete:
                access_list.append({"display_name": "得意先削除", "goto": "customer_delete"})
            if sales_access.order_aggregate_by_customer:
                access_list.append({"display_name": "得意先別受注集計", "goto": "order_aggregate_by_customer"})
            if sales_access.order_aggregate_management_by_product:
                access_list.append({"display_name": "製品別受注集計管理", "goto": "order_aggregate_management_by_product"})
            if sales_access.order_history_by_customer:
                access_list.append({"display_name": "得意先別受注履歴一覧", "goto": "order_history_by_customer"})
            if sales_access.order_history_by_product:
                access_list.append({"display_name": "商品別受注履歴一覧", "goto": "order_history_by_product"})

        personnel_access = Personnel.objects.filter(department=department, employee=self.employee_id).first()
        if personnel_access:
            if personnel_access.employee_information:
                access_list.append({"display_name": "従業員情報管理", "goto": "employee_information"})
            if personnel_access.division_information:
                access_list.append({"display_name": "部署情報管理", "goto": "division_information"})

        production_access = Production.objects.filter(department=department, employee=self.employee_id).first()
        if production_access:
            if production_access.production_information:
                access_list.append({"display_name": "生産情報管理", "goto": "production_management"})
            if production_access.inventory_management_product:
                access_list.append({"display_name": "製品在庫管理", "goto": "inventory_management"})
            if production_access.arrival_management_product:
                access_list.append({"display_name": "入荷管理", "goto": "arrival_management"})

        product_access = Product.objects.filter(department=department, employee=self.employee_id).first()
        if product_access:
            if product_access.product_information:
                access_list.append({"display_name": "製品情報", "goto": "product_info"})
            if product_access.inventory_information:
                access_list.append({"display_name": "在庫情報", "goto": "inventory_info"})
            if product_access.shipping_information:
                access_list.append({"display_name": "出荷情報", "goto": "shipping_info"})

        return access_list


class Sales(models.Model):
    order_information = models.BooleanField(default=True)
    customer_management = models.BooleanField(default=True)
    customer_edit = models.BooleanField(default=True)
    customer_delete = models.BooleanField(default=True)
    order_aggregate_by_customer = models.BooleanField(default=True)
    order_aggregate_management_by_product = models.BooleanField(default=True)
    order_history_by_customer = models.BooleanField(default=True)
    order_history_by_product = models.BooleanField(default=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return employee.employee_name


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

class Customer(models.Model):
    customer_id = models.CharField(max_length=6, primary_key=True)
    customer_name = models.CharField(max_length=200)
    tel_number = models.CharField(max_length=15)
    postal_code = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    mail = models.EmailField(max_length=200)
    responsible_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer_name
