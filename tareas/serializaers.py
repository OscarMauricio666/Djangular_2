from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.password = validated_data.get('password')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError('Este nombre de Ususario ya existe, intente otro')
        else:
            return data

    def validate_email(self, data):
        email = User.objects.filter(email = data)
        if len(email) != 0:
            raise serializers.ValidationError('Este email ya esta en uso, intente otro')
        else:
            return data
