from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length=30, required=False)
    mail_address = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)