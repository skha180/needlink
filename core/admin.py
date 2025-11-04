# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import CustomUser, ClientProfile, ProviderProfile, KYCVerification

# Minimal CustomUser admin using Django's UserAdmin as base
@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    model = CustomUser
    list_display = ("email", "user_type", "is_staff", "is_superuser", "is_active")
    list_filter = ("user_type", "is_staff", "is_superuser", "is_active")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("phone",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

# Register profiles and KYC
@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "city", "country")
    search_fields = ("full_name", "user__email")

@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "user", "business_name", "verified", "rating", "completed_jobs")
    list_filter = ("verified",)
    search_fields = ("full_name", "user__email", "business_name")

@admin.register(KYCVerification)
class KYCVerificationAdmin(admin.ModelAdmin):
    list_display = ("provider", "status", "submitted_at", "verified_at")
    list_filter = ("status",)
    search_fields = ("provider__user__email",)
