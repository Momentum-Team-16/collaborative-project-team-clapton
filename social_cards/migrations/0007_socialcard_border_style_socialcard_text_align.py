# Generated by Django 4.1.6 on 2023-02-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_cards', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcard',
            name='border_style',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='socialcard',
            name='text_align',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
