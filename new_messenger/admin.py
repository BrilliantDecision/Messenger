from django.contrib import admin
from new_messenger.models import Chat, ChatUsers, ChatUser, Messages


# Register your models here.
@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name', 'admin', 'create_date', 'private')
    list_display_links = ('name', )


@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'last_login', 'is_active')
    list_display_links = ('login', 'email', 'last_login', 'is_active')


@admin.register(ChatUsers)
class ChatUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat')
    list_display_links = ('user', 'chat')


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat', 'send_date')
    list_display_links = ('user', 'chat', 'send_date')
