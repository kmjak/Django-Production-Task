from django.shortcuts import render, redirect
from .forms import EmployeeLoginForm
from .models import Employee, Sales, Personnel, Production, Product, Customer

def login(request):
    if 'employee_id' in request.session:
        employee_id = request.session.get('employee_id')
        user = Employee.objects.filter(employee_id=employee_id).first()
        if user is not None:
            return redirect('/employee/home')
    params = {
        'title': 'Login',
        'subtitle': 'Login',
        'login_user': 'anonymous',
        'message': '',
        'id': '',
        'name': '',
        'form': EmployeeLoginForm(),
    }

    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        params['form'] = form
        if form.is_valid():
            id = form.cleaned_data['employee_id']
            name = form.cleaned_data['employee_name']
            password = form.cleaned_data['employee_password']

            user = Employee.objects.filter(employee_id=id, employee_name=name, employee_password=password).first()
            if user is not None:
                request.session['employee_id'] = user.employee_id
                request.session.modified = True
                return redirect('/employee/home')
            else:
                params['message'] = 'ログインに失敗しました。'
        else:
            params['message'] = 'フォームに誤りがあります。'

    return render(request, 'employee/index.html', params)

def logout(request):
    if 'employee_id' in request.session:
        del request.session['employee_id']
    return redirect('login')


def home(request):
    params = {
        'title': 'HOME',
        'subtitle': '機能一覧',
        'login_user': 'anonymous',
        'feature': [],
    }

    employee_id = request.session.get('employee_id')
    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            params['login_user'] = employee.employee_name
            access_list = employee.getAccessList()
            access_list.remove({"display_name": "得意先編集", "goto": "customer_edit"})
            access_list.remove({"display_name": "得意先削除", "goto": "customer_delete"})
            params['feature'] = access_list

        except Employee.DoesNotExist:
            return redirect('/employee/login')

    if params['login_user'] == "anonymous":
        return redirect('/employee/login')

    return render(request, 'employee/home.html', params)

def customers_list(request):
    params = {
        'title': '[得意先情報: 一覧]',
        'subtitle': '得意先情報: 一覧',
        'login_user': 'anonymous',
        'customers': [],
    }

    employee_id = request.session.get('employee_id')
    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            access_list = employee.getAccessList()
            isAccess = False
            for access in access_list:
                if access['goto'] == 'customer_management':
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')
            params['login_user'] = employee.employee_name

        except Employee.DoesNotExist:
            return redirect('/employee/login')

    customer = Customer.objects.all()
    params['customers'] = customer

    if params['login_user'] == "anonymous":
        return redirect('/employee/login')
    
    return render(request, 'employee/customers_list.html', params)

def customer_details(request, pk):
    params = {
        'title': '[得意先情報: 詳細]',
        'subtitle': '得意先情報: 詳細',
        'login_user': 'anonymous',
        'customer': [],
    }
    employee_id = request.session.get('employee_id')

    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            access_list = employee.getAccessList()
            isAccess = False
            for access in access_list:
                if access['goto'] == 'customer_management':
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')
            params['login_user'] = employee.employee_name
        except Employee.DoesNotExist:
            return redirect('/employee/login')

    if params['login_user'] == "anonymous":
        return redirect('/employee/login')

    if params['login_user'] != "anonymous":
        customer = Customer.objects.get(pk=pk)
        params['title'] = '[得意先情報: 詳細] ' + customer.customer_name
        params['customer'] = customer

    return render(request, 'employee/customer_details.html', params)

def customer_edit(request, pk):
    params = {
        'title': '[得意先情報: 編集]',
        'subtitle': '得意先情報: 編集',
        'login_user': 'anonymous',
        'customer': [],
        'employees': Sales.objects.all(),
    }
    employee_id = request.session.get('employee_id')

    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            access_list = employee.getAccessList()
            isAccess = False
            for access in access_list:
                if access['goto'] == 'customer_edit':
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')
            params['login_user'] = employee.employee_name
        except Employee.DoesNotExist:
            return redirect('/employee/login')

    if params['login_user'] == "anonymous":
        return redirect('/employee/login')

    if request.method == 'POST':
        customer = Customer.objects.get(pk=pk)
        customer.customer_name = request.POST['customer_name']
        customer.tel_number = request.POST['tel_number']
        customer.postal_code = request.POST['postal_code']
        customer.address = request.POST['address']
        customer.mail = request.POST['mail']
        customer.responsible_employee_id = request.POST['responsible_employee']
        customer.save()
        return redirect('/employee/customer_management/' + pk)

    if params['login_user'] != "anonymous":
        customer = Customer.objects.get(pk=pk)
        params['title'] = '[得意先情報: 詳細] ' + customer.customer_name
        params['customer'] = customer

    return render(request, 'employee/customer_edit.html', params)

def customer_delete(request, pk):
    employee_id = request.session.get('employee_id')
    
    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            access_list = employee.getAccessList()
            isAccess = False
            for access in access_list:
                if access['goto'] == 'customer_delete':
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')
        except Employee.DoesNotExist:
            return redirect('/employee/login')
    else:
        return redirect('/employee/login')

    if request.method == 'POST':
        customer = Customer.objects.get(pk=pk)
        customer.delete()
    return redirect('/employee/customer_management/')