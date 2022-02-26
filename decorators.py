from functools import wraps
from django.contrib import messages
from django.http import request
def my_decorator(f):
    @wraps(f)
    def wrapper(request,*args, **kwds):
        messages.info(request, 'نام کاربری یا رمز عبور اشتباه است')
        return f(request,*args, **kwds)
    return wrapper