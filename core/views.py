from django.shortcuts import render


def Room(request):
    return render(request, 'room.html', {'room_name':'hola'})

# Create your views here.
