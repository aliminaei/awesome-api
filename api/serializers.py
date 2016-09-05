from models import *
from rest_framework import serializers


class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = ('username', 'first_name', 'last_name', 'email', "password")
        extra_kwargs =  {
            'username': {'max_length':254, 'min_length':3, 'allow_blank':False, 'trim_whitespace':True, 'allow_null':False, 'required':True}, 
            'email': {'max_length':254, 'min_length':3, 'allow_blank':False, 'trim_whitespace':False, 'allow_null':False, 'required':True}, 
            'password': {'write_only': True, 'max_length':254, 'min_length':3}, 
            'first_name': {'allow_null': True, 'allow_blank': True, 'max_length':254, 'required':False}, 
            'last_name': {'allow_null': True, 'allow_blank': True, 'max_length':254, 'required':False}
        }

class UserSerializer(serializers.Serializer):
    username   = serializers.CharField(max_length=254, min_length=3, allow_blank=False, trim_whitespace=True, allow_null=False, required=True)
    email      = serializers.EmailField(max_length=254, allow_blank=False, trim_whitespace=False, allow_null=False, required=True)
    password   = serializers.CharField(max_length=254, min_length=3, allow_blank=False, trim_whitespace=True, allow_null=False, required=True, write_only=True, style={'input_type': 'password'})
    first_name = serializers.CharField(max_length=254, allow_blank=True, allow_null=True, required=False)
    last_name  = serializers.CharField(max_length=254, allow_blank=True, allow_null=True, required=False)

    def create(self, validated_data):
        return APIUser(**validated_data)

