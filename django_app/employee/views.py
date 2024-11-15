from django.shortcuts import render, redirect
from .forms import EmployeeLoginForm
from .models import Employee

def login(request):
    if 'employee_id' in request.session:
        employee_id = request.session.get('employee_id')
        user = Employee.objects.filter(employee_id=employee_id).first()
        if user is not None:
            return redirect('/employee/home')
    params = {
        'title': 'Login',
        'login_user': 'annoymous',
        'is_login': False,
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
