from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1 style="background-color:black;color:yellowgreen;text-align:center" >Back-End Todo App :)</h1>')