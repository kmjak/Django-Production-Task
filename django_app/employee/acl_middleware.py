from django.shortcuts import redirect
from .models import Employee

class AclMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        employee_id = request.session.get('employee_id')
        user = Employee.objects.filter(employee_id=employee_id).first()
        path = request.path
        request.user = user
        if user is None:
            if not path.startswith('/employee/login'):
                return redirect('/employee/login')
        else:
            acl = user.getAccessList()
            goto = path[10:]
            isAccess = False
            if goto == 'home':
                isAccess = True
            for access in acl:
                if goto.startswith(access['goto']):
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')

        response = self.get_response(request)

        return response
