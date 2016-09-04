from models import *
from rest_framework import serializers


class ApiUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = API_User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', )
        read_only_fields = ('id',)
