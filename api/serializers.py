from models import *
from rest_framework import serializers
from hasher import hash_password


class ApiUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = API_User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', "password")
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = API_User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.password = hash_password(validated_data['password'])
        user.save()
        return user
