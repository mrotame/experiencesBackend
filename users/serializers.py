from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models.users import Users

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Users
        fields = [
            'id',
            'nome',
            'email',
            "password"
        ]
        extra_kwargs = {'nome': {'required': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class SessionLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email',
            'password'
        ]