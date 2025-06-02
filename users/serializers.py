from rest_framework import serializers
from users.models import CustomUser
from users.serializers import UserSerializer



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label="Confirm password")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name', 'phone_number', 'user_type')
        extra_kwargs = {
            'first_name': {'required': False}, 'last_name': {'required': False},
            'phone_number': {'required': False}, 'user_type': {'required': False, 'default': 'customer'}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "This email is already registered."})
        # Add username uniqueness check if username is not email
        if attrs.get('username') != attrs.get('email') and CustomUser.objects.filter(username=attrs['username']).exists():
             raise serializers.ValidationError({"username": "This username is already taken."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'profile_picture', 'user_type')
