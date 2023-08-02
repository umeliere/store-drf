from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminModel
from users.models import User
from django.utils.translation import gettext_lazy as _


class UserAdmin(UserAdminModel):
    fieldsets = (
        (None, {"fields": ("username", "slug", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "address", "phone", "city")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "slug", "email", "first_name", "last_name", "email", "address", "phone", "city")


admin.site.register(User, UserAdmin)
