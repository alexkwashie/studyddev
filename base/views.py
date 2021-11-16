from django.shortcuts import render
from .models import Room
# Create your views here.



def homepage(request):
    room = Room.objects.all()
    return render(request,'base/home.html', {'room':room} )

def roompage(request, pk):
    room1 = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room':room1} )
