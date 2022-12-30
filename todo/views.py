from django.shortcuts import  get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status


from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method=='GET':
        # todos=Todo.objects.all()
        todos=Todo.objects.filter(is_done=False)
        # tamamlanmayan task'leri getir (filtrele)
        serializer=TodoSerializer(todos,many=True)
        #  (many=True) veri querySet formatinda oldugu icin yazilir.
        return Response(serializer.data)
    elif request.method=='POST':
        # burada db'den veri çekmiyorum,db'ye veri gönderiyorum.bu yüzden gelen veriyi direkt serializer'a sokuyorum
        serializer=TodoSerializer(data=request.data)
        # db'ye kaydetmeden önce verinin gecerli oldugunu kontrol etmem lazım
        if serializer.is_valid():
            serializer.save()
            message='Data posted successfully!'
            
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def todo_detail(request,pk):
    todos=get_object_or_404(Todo,id=pk)
    if request.method=='GET':
        # todos=Todo.objects.get(id=pk)
        # eger girilen gecerli bir id degilse hata verecektir.bunu önlemek icin try-catch vazifesi gören get_object_or_404 fonksiyonu kullanilabilir
        # todos=get_object_or_404(Todo,id=pk) DRY
        serializer=TodoSerializer(todos)
        return Response(serializer.data)
        # many=True demeye gerek yok.querySet dönmüyor tek bir veri döndüğü için
    if request.method=='PUT':
        # todos=get_object_or_404(Todo,id=pk) DRY
        serializer=TodoSerializer(instance=todos,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        # todos=get_object_or_404(Todo,id=pk) DRY
        todos.delete()
        # best practice for comment in json type hmmm :)
        message={
            "message":"Data deleted successfully!"
        }
        return Response(message)


# ! Concrete Views

class TodoCV(ListCreateAPIView):
    queryset=Todo.objects.filter(is_done=False)
    serializer_class=TodoSerializer

class TodoDetailCV(RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer


        

         

    

    






