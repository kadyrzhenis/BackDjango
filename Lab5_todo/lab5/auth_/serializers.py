from rest_framework import serializers
from auth_.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')