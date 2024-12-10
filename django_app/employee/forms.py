from django import forms
from .models import Employee

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField(
        max_length=6,
        label="従業員ID",
        widget=forms.TextInput(attrs={
            'class': 'block border-2 border-black rounded-lg w-full px-3 py-1 opacity-30 hover:opacity-50 focus:opacity-100 transition-all',
            'id': 'employee-id',
            })
    )
    employee_name = forms.CharField(
        max_length=200,
        label="従業員名",
        widget=forms.TextInput(attrs={
            'class': 'block border-2 border-black rounded-lg w-full px-3 py-1 opacity-30 hover:opacity-50 focus:opacity-100 transition-all',
            'id': 'employee-name',
        })
    )
    employee_password = forms.CharField(
        max_length=200,
        label="パスワード",
        widget=forms.PasswordInput(attrs={
            'class': 'block border-2 border-black rounded-lg w-full px-3 py-1 opacity-30 hover:opacity-50 focus:opacity-100 transition-all',
            'id': 'password',
        })
    )

class CustomerSearchForm(forms.Form):
    customer_id = forms.CharField(
        max_length=6,
        label="得意先ID",
        widget=forms.TextInput(attrs={
            'class': 'block border-2 border-black rounded-lg w-full px-3 py-1 opacity-30 hover:opacity-50 focus:opacity-100 transition-all',
            'id': 'customer-id',
        })
    )