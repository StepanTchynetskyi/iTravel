from rest_framework import serializers
from models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=55, null=False, blank=False)
    last_name = serializers.CharField(max_length=55, null=False, blank=False)
    email = serializers.EmailField(max_length=100, null=False, blank=False)
    password = serializers.CharField(max_length=128, null=False, blank=False)
    created = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.title)
        instance.last_name = validated_data.get('last_name', instance.code)
        instance.email = validated_data.get('email', instance.linenos)
        instance.password = validated_data.get('password', instance.language)
        instance.save()
        return instance
