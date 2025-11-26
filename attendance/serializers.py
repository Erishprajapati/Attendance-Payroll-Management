from .models import * 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser
from rest_framework.validators import UniqueValidator
from datetime import date
"""
serializer to show role and username while logging
"""
class CustomTokenObtainPair(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    def validate(self,attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField() #charfield for storing passwords
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])#email must for login so required is made as True
    username = serializers.CharField(required = True, validators =[UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(write_only = True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    date_of_birth = serializers.DateField(required = True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'date_of_birth')
        extra_kwagrs ={
            'password':{'write_only':True},
            'password_confirm':{'write_only':True}
        }
    def validate_date_of_birth(self,value):
        dob = value.date() if hasattr(value, "date") else value
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in future")
        return value

    def validate(self,data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password": 'Password dont match'})
        return data
    
    def create(self,validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            is_verified = False
        )
        return user
