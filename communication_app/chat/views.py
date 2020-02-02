# chat/views.py
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import json
from . models import messages,rooms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Friend

@login_required(login_url='/users/login/') #redirect when user is not logged in
def index(request):
    return render(request, 'chat/index.html')


def render_messages(room_name):
    if rooms.objects.filter(name = room_name).exists():
        room_id = rooms.objects.get(name=room_name).id  
        return list(messages.objects.filter(room_id=room_id).values())

@login_required(login_url='/users/login/') #redirect when user is not logged in
def room(request, room_name):
    users = User.objects.exclude(id=request.user.id)
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        friends = []

    args = {'users': users, 'friends' : friends}
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'prev_messages' : render_messages(room_name),
        'users' :users,
        'friends' :friends,
        'room_name' :room_name,
    })

@login_required
def change_friends(request, operation, pk, room_name):
    room_name = room_name.replace("\"","")
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return room(request, room_name)
