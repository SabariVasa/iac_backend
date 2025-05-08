from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    phone_number = serializers.RegexField(regex=r'^\+?\d{10,15}$')
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)

    def validate(self, data):
        if User.objects(username=data['username']).first():
            raise serializers.ValidationError("Username already exists.")
        if User.objects(email=data['email']).first():
            raise serializers.ValidationError("Email already registered.")
        if User.objects(phone_number=data['phone_number']).first():
            raise serializers.ValidationError("Phone number already registered.")
        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects(email=data['email']).first()
        if not user or not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid credentials.")
        return data
