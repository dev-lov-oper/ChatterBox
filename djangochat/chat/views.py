from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    return render(request, 'room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if room.objects.filter(name=room).exists():
        #  query paramater is used to pass data from one view to another view
         return redirect('/'+room+'/?username='+username)
    else:
            new_room = Room.objects.create(name=room)
            new_room.save()
        

    return render(request, 'room.html', {'room': room, 'username': username})
