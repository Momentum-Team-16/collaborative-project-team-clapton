from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SocialCard
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm


# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(SocialCard)
