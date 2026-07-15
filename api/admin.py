from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


# Inline profile inside User
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


# Extend User admin
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


# Unregister default User
admin.site.unregister(User)

# Register new User admin
admin.site.register(User, CustomUserAdmin)