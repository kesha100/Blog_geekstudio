from django.contrib.auth import authenticate
from rest_framework import serializers

from user.models import MyUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords do not match!')
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        return user




