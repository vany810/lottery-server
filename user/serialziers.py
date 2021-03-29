from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'wechat_avatar')

    def validate_username(self, username):
        if User.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError('用户名已存在')

        return username

    def save(self, *args, **kwargs):
        user = User(**self.validated_data)
        user.set_password('123456')
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'avatar', 'wechat_avatar')
