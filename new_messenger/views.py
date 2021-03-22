import json

from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from new_messenger.models import Chat, ChatUsers, ChatUser, Messages
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
# authentication view
# @method_decorator(csrf_exempt)
def authentication(request):
    login_or_email = request.GET.get('login_or_email')
    password = request.GET.get('password')
    if login_or_email and password:
        obj1 = ChatUser.objects.filter(login=login_or_email, password=password).first()
        if obj1:
            return redirect(f'/get_user_chats/{obj1.id}/')
        obj1 = ChatUser.objects.filter(email=login_or_email, password=password).first()
        if obj1:
            return redirect(f'/get_user_chats/{obj1.id}/')
        else:
            return JsonResponse({'detail': 'Incorrect login/email or password'})
    else:
        return JsonResponse({'detail': 'Missing arguments'})


# get chats for user
def get_user_chats(request, user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return JsonResponse({'detail': 'Only int allowed'})
    chat_ids = list(ChatUsers.objects.filter(user=user_id).values_list('chat_id', flat=True))
    if len(chat_ids) == 0:
        return JsonResponse({"detail": 'No chats for user'})
    chats = Chat.objects.filter(pk__in=chat_ids)
    res = []
    for chat in chats:
        res.append({
            'id': chat.id,
            'name': chat.name,
            'create_date': chat.create_date,
        })
    return JsonResponse({'detail': 'OK', 'user_id': user_id, 'data': res})


# get users for chat
def get_chat_users(request, chat_id):
    try:
        chat_id = int(chat_id)
    except ValueError:
        return JsonResponse({'detail': 'Only int allowed'})
    user_ids = list(ChatUsers.objects.filter(chat_id=chat_id).values_list('user_id', flat=True))
    if len(user_ids) == 0:
        return JsonResponse({'detail': "No chat with that id"})
    users = ChatUser.objects.filter(pk__in=user_ids)
    res = []
    for user in users:
        res.append({
            'id': user.id,
            'login': user.login,
        })
    return JsonResponse({'detail': 'OK', 'chat_id': chat_id, 'data': res})


# get messages for chat
def get_chat_messages(request, chat_id):
    try:
        chat_id = int(chat_id)
    except ValueError:
        return JsonResponse({'detail': 'Only int allowed'})
    try:
        Chat.objects.get(id=chat_id)
    except ObjectDoesNotExist:
        return JsonResponse({'detail': "No chat with that id"})
    messages = Messages.objects.filter(chat_id=chat_id).order_by('pk')
    res = []
    for message in messages:
        res.append({
            'user_id': message.user.id,
            'login': message.user.login,
            'date': message.send_date.strftime('%d.%m.%Y, %H:%M'),
            'text': message.text,
        })
    return JsonResponse({'detail': 'OK', 'chat_id': chat_id, 'data': res})
