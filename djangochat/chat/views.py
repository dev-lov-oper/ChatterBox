from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chat.models import Room, Message

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {'username': username, 'room': room, 'room_details': room_details})

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room_name).exists():
        #  query paramater is used to pass data from one view to another view
        return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()

    return render(request, 'room.html', {'room': room_name, 'username': username})


def send(request):
    message_text = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    room = Room.objects.get(id=room_id)
    new_message = Message.objects.create(value=message_text, user=username, room=room.name)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.name)
    return JsonResponse({"messages": list(messages.values())})