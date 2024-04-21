from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'firstname', 'lastname', 'phone', 'email', 'password']  # firstname, lastname, phone, email ve password alanlarını belirttim

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
