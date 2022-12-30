from django.urls import path
from .views import (
    todo_list_create,
    todo_detail,
    TodoCV,
    TodoDetailCV
)


urlpatterns = [

    # path('todo-list/',todo_list_create),
    # path('todo_detail/<int:pk>',todo_detail)
    path('todo-list/',TodoCV.as_view()),
    path('todo_detail/<int:pk>',TodoDetailCV.as_view())
    
]
