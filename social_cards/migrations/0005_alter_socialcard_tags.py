# Generated by Django 4.1.6 on 2023-02-02 21:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('social_cards', '0004_follower_created_follower_followed_follower_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialcard',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]