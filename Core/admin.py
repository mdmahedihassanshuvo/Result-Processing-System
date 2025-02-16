from django.contrib import admin

# LOCAL IMPORTS
from Core.models import CustomUser, UserCategory


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'full_name'
    ]
    search_fields = ['id', 'email',]
    ordering = ['id',]


@admin.register(UserCategory)
class UserCategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'category'
    ]
    search_fields = ['user', 'category']
    ordering = ['user',]
