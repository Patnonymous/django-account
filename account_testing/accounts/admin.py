from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Import models and forms here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
