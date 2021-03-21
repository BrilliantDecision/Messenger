from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView

from new_messenger.models import Chat, ChatUsers, ChatUser, Messages
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class Authentication(FormView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        login_or_email = request.POST.get('login_or_email')
        password = request.POST.get('password')
        obj1 = get_user_model().objects.filter(username=login_or_email, password=password).first()
        obj2 = get_user_model().objects.filter(email=login_or_email, password=password).first()
        return JsonResponse({'detail': 'OK'})
