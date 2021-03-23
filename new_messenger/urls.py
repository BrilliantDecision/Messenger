from django.urls import path, include
from new_messenger import views


urlpatterns = [
    path('check_login/', views.check_login),
    path('registration/', views.registration),
    path('authentication/', views.authentication),
    path('get_user_chats/<user_id>/', views.get_user_chats),
    path('get_chat_users/<chat_id>/', views.get_chat_users),
    path('get_chat_messages/<chat_id>/', views.get_chat_messages),
]


