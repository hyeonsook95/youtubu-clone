from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("avatar", "gender", "birthdate",)},),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "count_channels",
        "is_staff",
        "is_superuser",
    )
