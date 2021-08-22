import pytest

# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIClient
# from rest_framework import status
#
# from django.contrib.auth.models import User
# from django.urls import reverse
#
# import requests
# import json
# from jsonschema import validate
# from jsonschema import Draft6Validator
#
#
#
#
# class CL:
#     def __init__(self, usert):
#         Token.objects.get_or_create(user=usert)
#         self.token = Token.objects.get(user=usert)
#         client = APIClient()
#         client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#         return client
#
# @pytest.fixture
# def CL_authenticate():
#     usert = User.objects.get(id=1)
#     return CL(usert)
#
#
# def test_path_get_variable(CL_authenticate):
#     # get API response
#     response = CL_authenticate.get(reverse('variable'))
#     print(response)
#     # self.assertEqual(response.request['PATH_INFO'], '/variable/')

# def test_path_get_course(self):
#     # get API response
#     response = self.client.get(reverse('course'))
#     self.assertEqual(response.request['PATH_INFO'], '/course/')
#
# def test_path_get_experience(self):
#     # get API response
#     response = self.client.get(reverse('experience'))
#     self.assertEqual(response.request['PATH_INFO'], '/experience/')
#
# def test_path_get_education(self):
#     # get API response
#     response = self.client.get(reverse('education'))
#     self.assertEqual(response.request['PATH_INFO'], '/education/')