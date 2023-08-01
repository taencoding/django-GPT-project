from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'nickname', 'password']

class SignUpSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'nickname', 'password1', 'password2']

    def validate(self, data):
        # 비밀번호 검사
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        
        # 기존 사용자 중복 검사
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("이미 사용중인 이메일입니다.")
        
        return data
        
    def create(self, validated_date):
        user = User.objects.create_user(
            email = validated_date['email'],
            nickname = validated_date['nickname'],
            password = validated_date['password1']
        )
        return user