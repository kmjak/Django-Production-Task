from django.shortcuts import redirect
from .models import Employee

class AclMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        path = request.path

        employee_id = request.session.get('employee_id')
        user = Employee.objects.filter(employee_id=employee_id).first()

        if user is None:
            if not path.startswith('/employee/login'):
                return redirect('/employee/login')
        else:
            acl = user.getAccessList()
            goto = path[10:]
            print(goto)
            print("-------")
            isAccess = False
            if goto == 'home':
                isAccess = True
            for access in acl:
                print(access['goto'])
                if access['goto'] + "/" == goto:
                    isAccess = True
                    break
            if not isAccess:
                return redirect('/employee/home')
        return response
