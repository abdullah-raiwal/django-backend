from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models  # Import your User model from the appropriate location

class UserAdmin(BaseUserAdmin):

    ordering = ['id']
    list_display = ['email', 'name', 'is_active', 'is_staff']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups')
    filter_horizontal = ('groups', 'user_permissions')

# Register the custom UserAdmin with your User model
admin.site.register(models.User, UserAdmin)
