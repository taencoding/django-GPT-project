from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_date):
        user = User.objects.create_user(
            email = validated_date['email'],
            nickname = validated_date['nickname'],
            password = validated_date['password']
        )
        return user

    class Meta:
        model = User
        fields = ['email, nickname, password']
        