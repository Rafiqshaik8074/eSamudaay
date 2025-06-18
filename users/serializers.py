# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer

class LoginSerializer(serializers.Serializer):
    # email = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'phone', 'password']
