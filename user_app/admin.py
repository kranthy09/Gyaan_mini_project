# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# fieldsets = UserAdmin.fieldsets + (
#     (None, {'fields':('user_role', 'profile_pic')}),
# )
admin.site.register(User, UserAdmin)
