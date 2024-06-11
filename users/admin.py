from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm
from .filters import RoleFilter


class CustomUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + (RoleFilter,)
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role',),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)