from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class ChatUser(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='profile_user', on_delete=models.CASCADE, null=True)
    status = models.TextField('Text', max_length=100)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Additional user information'
        verbose_name_plural = 'Additional user information'


class Chat(models.Model):
    name = models.CharField('Name', max_length=100)
    admin = models.ForeignKey(get_user_model(), related_name='user_admin', on_delete=models.CASCADE, null=True)
    create_date = models.DateField('Create date', null=True)
    private = models.BooleanField('Is private', default=False)

    def __str__(self):
        return f'Chat name: {self.name}'

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


class ChatUsers(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='chat_users_user', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, related_name='chat_users_chat', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'User: {self.user}, Chat: {self.chat}'

    class Meta:
        verbose_name = 'Chat users'
        verbose_name_plural = 'Chat users'

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'chat'],
                name='chat_user constraint'
            )
        ]


class Messages(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='messages_user', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, related_name='messages_chat', on_delete=models.CASCADE, null=True)
    text = models.TextField('Text', max_length=500)
    send_date = models.DateTimeField('Send date', null=True)

    def __str__(self):
        return f'User: {self.user}, Chat: {self.chat}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
