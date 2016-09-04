from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response
from models import *
from serializers import *


@csrf_exempt
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    List all API users, or create a new API user.
    """
    if request.method == 'GET':
        users = APIUser.objects.all()
        serializer = ApiUserSerializer(users, many=True)
        return response.Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print data
        serializer = ApiUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)

@csrf_exempt
@api_view(['GET', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve or delete an API user.
    """
    try:
        user = APIUser.objects.get(pk=pk)
    except APIUser.DoesNotExist:
        return response.Response(status=404)

    if request.method == 'GET':
        serializer = ApiUserSerializer(user)
        return response.Response(serializer.data)

    elif request.method == 'DELETE':
        if 'HTTP_API_SECRET' not in request.META:
            data = {}
            data["details"] = "api-secret were not provided."
            return response.Response(status=401, data=data)
        if reques.META['HTTP_API_SECRET'] != settings.API_SECRET_KEY:
            data = {}
            data["details"] = "Invalid api-secret."
            return response.Response(status=401, data=data)

        user.delete()
        return response.Response(status=204)
