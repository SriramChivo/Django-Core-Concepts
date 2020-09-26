from django.http import HttpResponse
from django.shortcuts import redirect


def allowedusers(allowedroles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('working')
            # group = None
            # print(allowedroles)
            check = request.user.groups.all()
            # print(check)
            for i in check:
                # print(i)
              # bot are same with name or without
                if(i.name in allowedroles):
                    # print('True')
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('No Permission to view this page')
                # print(i.name)
            # print(check)

        return wrapper_func
    return decorator
