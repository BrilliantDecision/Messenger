from django.db import models


# Create your models here.
class ChatUser(models.Model):
    login = models.CharField('Login', max_length=100)
    password = models.CharField('password', max_length=100)
    email = models.EmailField('Email', default='')
    first_name = models.CharField('First name', default='', max_length=100)
    second_name = models.CharField('Second_name', default='', max_length=100)
    status = models.TextField('Text', max_length=100)
    is_active = models.BooleanField('Is active', default=True)
    last_login = models.DateTimeField('Last login', null=True)
    image = models.ImageField('Фото', upload_to=f'users/')

    def __str__(self):
        return f'{self.login}'

    class Meta:
        verbose_name = 'Our user'
        verbose_name_plural = 'Our user'


class Chat(models.Model):
    name = models.CharField('Name', max_length=100)
    admin = models.ForeignKey(ChatUser, related_name='user_admin', on_delete=models.CASCADE, null=True)
    create_date = models.DateField('Create date', null=True)
    private = models.BooleanField('Is private', default=False)
    image = models.ImageField('Фото', upload_to='chats/')

    def __str__(self):
        return f'Chat name: {self.name}'

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'


class ChatUsers(models.Model):
    user = models.ForeignKey(ChatUser, related_name='chat_users_user', on_delete=models.CASCADE, null=True)
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
    user = models.ForeignKey(ChatUser, related_name='messages_user', on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, related_name='messages_chat', on_delete=models.CASCADE, null=True)
    text = models.TextField('Text', max_length=500)
    send_date = models.DateTimeField('Send date', null=True)

    def __str__(self):
        return f'User: {self.user}, Chat: {self.chat}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
