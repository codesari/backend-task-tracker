from django.urls import path
from .views import todo_home

urlpatterns = [
    
    path('',todo_home)
]
