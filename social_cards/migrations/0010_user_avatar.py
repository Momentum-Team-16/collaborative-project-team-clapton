# Generated by Django 4.1.6 on 2023-02-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_cards', '0009_socialcard_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars'),
        ),
    ]
