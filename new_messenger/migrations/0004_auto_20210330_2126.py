# Generated by Django 3.1.7 on 2021-03-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_messenger', '0003_auto_20210330_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='image',
            field=models.ImageField(null=True, upload_to='chats/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='chatuser',
            name='image',
            field=models.ImageField(null=True, upload_to='users/', verbose_name='Фото'),
        ),
    ]