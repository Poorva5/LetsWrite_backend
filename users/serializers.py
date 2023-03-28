from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from users.models import User

class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta:
        model = User
        fields  = ['email', 'id', 'first_name', 'last_name']
