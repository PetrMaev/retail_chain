from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "avatar", "phone_number", "country", "is_active")
    search_fields = ("email",)
