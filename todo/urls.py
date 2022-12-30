from django.urls import path,include
from rest_framework import routers
from .views import (
    todo_list_create,
    todo_detail,
    TodoCV,
    TodoDetailCV,
    TodoMVS
)

router = routers.DefaultRouter()
router.register("todo", TodoMVS)
# router.register("todo/<int:pk>", TodoMVS)



urlpatterns = [

    # path('todo-list/',todo_list_create),
    # path('todo_detail/<int:pk>',todo_detail)
    # path('todo-list/',TodoCV.as_view()),
    # path('todo_detail/<int:pk>',TodoDetailCV.as_view())
    
    # ! Model View Set
    path("",include(router.urls))  
]
