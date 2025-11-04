from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, ClientProfile, ProviderProfile


# ---------------------------
# User Registration Serializer
# ---------------------------
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'user_type', 'phone']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type', 'client'),
            phone=validated_data.get('phone', '')
        )

        # Create profile automatically
        if user.user_type == 'client':
            ClientProfile.objects.create(user=user, full_name=user.email)
        else:
            ProviderProfile.objects.create(user=user, full_name=user.email)

        return user


# ---------------------------
# User Login Serializer
# ---------------------------
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")
        return user


# ---------------------------
# User Profile Serializer
# ---------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'user_type', 'phone', 'is_verified', 'date_joined']
