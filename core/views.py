from django.shortcuts import render

def index(request):
    return render(request, 'base.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
# Create your views here.
