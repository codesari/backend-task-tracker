from django.http import HttpResponse
from .models import Todo

def todo_home(request):
    return HttpResponse('<h1 style="background-color:black;color:yellowgreen;text-align:center" >Todo App </h1>')

