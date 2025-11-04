from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# ==============================================================
# 1️⃣ Custom User Manager
# ==============================================================
class CustomUserManager(BaseUserManager):
    """Manager for custom user model with email as username."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Email field is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


# ==============================================================
# 2️⃣ Custom User Model
# ==============================================================
class CustomUser(AbstractUser):
    """Custom User model using email instead of username."""

    USER_TYPE_CHOICES = [
        ("client", "Client"),
        ("provider", "Service Provider"),
    ]

    username = None  # Disable username field
    email = models.EmailField(_("email address"), unique=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="client"
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # For email or KYC
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.user_type})"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


# ==============================================================
# 3️⃣ Abstract Base Profile
# ==============================================================
class BaseProfile(models.Model):
    """Abstract base class shared by all profile types."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="%(class)s_profile"
    )
    full_name = models.CharField(max_length=150)
    profile_photo = models.ImageField(
        upload_to="profile_photos/", blank=True, null=True
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.email} Profile"


# ==============================================================
# 4️⃣ Client Profile
# ==============================================================
class ClientProfile(BaseProfile):
    """Profile for normal service requesters."""

    preferred_services = models.ManyToManyField(
        "services.SubCategory", blank=True, related_name="interested_clients"
    )

    def __str__(self):
        return f"Client: {self.full_name or self.user.email}"


# ==============================================================
# 5️⃣ Provider Profile (Service Provider)
# ==============================================================
class ProviderProfile(BaseProfile):
    """Profile for service providers, includes KYC & verification."""

    business_name = models.CharField(max_length=150, blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    id_type = models.CharField(
        max_length=50, blank=True, null=True, help_text="Type of ID (e.g. NIN, Voter ID, Driver’s License)"
    )
    id_number = models.CharField(max_length=100, blank=True, null=True)
    id_document = models.FileField(upload_to="kyc_documents/", blank=True, null=True)
    verified = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    completed_jobs = models.PositiveIntegerField(default=0)
    total_reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        status = "✅ Verified" if self.verified else "❌ Unverified"
        return f"Provider: {self.full_name or self.user.email} ({status})"


# ==============================================================
# 6️⃣ KYC Verification Requests
# ==============================================================
class KYCVerification(models.Model):
    """Tracks service provider verification requests."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    provider = models.OneToOneField(
        ProviderProfile, on_delete=models.CASCADE, related_name="kyc_verification"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    admin_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"KYC: {self.provider.user.email} - {self.status}"

    class Meta:
        verbose_name = "KYC Verification"
        verbose_name_plural = "KYC Verifications"
