from models import *
from rest_framework import serializers


class ApiUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', "password")
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}, 'first_name': {'allow_null': True, 'allow_blank': True}, 'last_name': {'allow_null': True, 'allow_blank': True}}