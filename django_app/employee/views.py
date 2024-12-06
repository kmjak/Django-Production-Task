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
            params['feature'] = access_list

        except Employee.DoesNotExist:
            params['login_user'] = 'unknown user'

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
            params['login_user'] = employee.employee_name
        except Employee.DoesNotExist:
            params['login_user'] = 'unknown user'
    customer = Customer.objects.all()
    params['customers'] = customer

    return render(request, 'employee/customers_list.html', params)

def customer_details(request, pk):
    params = {
        'title': '[得意先情報: 一覧]',
        'subtitle': '得意先情報: 一覧',
        'login_user': 'anonymous',
        'customer': [],
    }
    employee_id = request.session.get('employee_id')

    if employee_id:
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            params['login_user'] = employee.employee_name
        except Employee.DoesNotExist:
            params['login_user'] = 'unknown user'
    if params['login_user'] != "anonymous":
        customer = Customer.objects.get(pk=pk)
        params['customer'] = customer

    return render(request, 'employee/customer_details.html', params)