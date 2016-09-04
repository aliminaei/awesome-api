from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from models import *

class APIUserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new api user object.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')

    def test_create_user_duplicate_username(self):
        """
        Ensure we cannot create a new api user object with the the same username.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')
        data = {"password": "Password1!","username": "ali","first_name": "ali2","last_name": "Minaei2","email": "ali.minaei2@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"username": ["APIUser with this username already exists."]})

    def test_create_user_blank_username(self):
        """
        Ensure we cannot create a new api user object with blank username.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"username": ["This field may not be blank."]})

    def test_create_user_no_username(self):
        """
        Ensure we cannot create a new api user object with no username.
        """
        url = '/api/users/'
        data = {"password": "Password1!","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"username": ["This field is required."]})

    def test_create_user_blank_password(self):
        """
        Ensure we cannot create a new api user object with blank password.
        """
        url = '/api/users/'
        data = {"password": "","username": "ali","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"password": ["This field may not be blank."]})

    def test_create_user_no_password(self):
        """
        Ensure we cannot create a new api user object with no password.
        """
        url = '/api/users/'
        data = {"username": "ali","first_name": "ali","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"password": ["This field is required."]})

    def test_create_user_blank_email(self):
        """
        Ensure we cannot create a new api user object with blank email.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","last_name": "Minaei","email": ""}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"email": ["This field may not be blank."]})

    def test_create_user_no_email(self):
        """
        Ensure we cannot create a new api user object with no email.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","last_name": "Minaei"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"email": ["This field is required."]})

    def test_create_user_blank_first_name(self):
        """
        Ensure we can create a new api user object with blank first_name.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "","last_name": "Minaei","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')

    def test_create_user_no_first_name(self):
        """
        Ensure we can create a new api user object with no first_name.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","last_name": "Minaei","email": "ali@minaei.me"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')

    def test_create_user_blank_last_name(self):
        """
        Ensure we can create a new api user object with blank last_name.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","last_name": "","email": "ali.minaei@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')

    def test_create_user_no_last_name(self):
        """
        Ensure we can create a new api user object with no last_name.
        """
        url = '/api/users/'
        data = {"password": "Password1!","username": "ali","first_name": "ali","email": "ali@minaei.me"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(APIUser.objects.count(), 1)
        self.assertEqual(APIUser.objects.get().username, 'ali')
