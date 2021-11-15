from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

room=[
    {'id':1, 'name': 'Python Boys in the house' },
    {'id':2, 'name': 'Machine Learning girls' },
    {'id':3, 'name': 'Tensorflow bosses' }
]


def homepage(request):
    return render(request,'base/home.html', {'room':room} )

def roompage(request, pk):
    room1 = None
    for i in room:
        if i['id'] == int(pk):
            room1 = i
    return render(request, 'base/room.html', {'room':room1} )
