from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework import renderers, response, schemas, generics, status
from rest_framework.authentication import *
import coreapi
from models import *
from serializers import *

class ListCreateUserView(generics.ListCreateAPIView):
    """
    List all API users, or create a new API user.
    """
    permission_classes = (AllowAny,)
    authentication_classes = ()
    queryset = APIUser.objects.all()
    serializer_class = ApiUserSerializer
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)


class UserDetail(APIView):
    """
    Retrieve or delete an API user for the given ID.
    To delete the API user you have to include your api secret in your request header.
    """

    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser,)

    def get_object(self, username):
        try:
            return APIUser.objects.get(pk=username)
        except APIUser.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = ApiUserSerializer(user)
        return response.Response(serializer.data)

    def delete(self, request, username, format=None):
        user = self.get_object(username)
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


@csrf_exempt
@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])
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
@renderer_classes([JSONRenderer])
def user_detail(request, username, format=None):
    """
    Retrieve or delete an API user for the given ID.
    To delete the API user you have to include your api secret in your request header.
    """
    try:
        user = APIUser.objects.get(pk=username)
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
