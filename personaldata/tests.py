from django.test import TestCase, Client
from .models import AboutDesc, Variable
from .views import  GetSocialMedia, GetEducation, GetExperience, GetCourse, GetVariables
from .serializers import VariableSerializer
# Create your tests here.

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

# Include an appropriate `Authorization:` header on all requests.


# # class to define a test case for login
class GetPersonalDataTestCase(TestCase):
    def setUp(self):
        about_desc = AboutDesc.objects.create(
            content="",
            purpose="",
            is_publish=False
        )
        about_desc_pub = AboutDesc.objects.create(
            content="",
            purpose="",
            is_publish=True
        )
        username = "admin"
        password = "bar"
        user = User.objects.create_user(username=username, password=password)
        usert = User.objects.get(id=user.id)
        Token.objects.get_or_create(user=usert)
        self.token = Token.objects.get(user=usert)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        varData = [
            {'name': "namevar1", 'value': "valuevar1"},
            {'name': "namevar2", 'value': "valuevar2"}
        ]
        for data in varData:
            Variable.objects.create(
                name=data["name"],
                value=data["value"]
            )
        # print(about_desc)

    def test_get_content_about(self):
        about_count = AboutDesc.objects.all().count()
        about_published_count = AboutDesc.objects.filter(is_publish=True).count()
        self.assertNotEqual(about_count, 0)
        self.assertEqual(about_published_count, 1)

    def test_response_variables(self):
        # get API response
        response = self.client.get(reverse('variable'))
        # print(response.__dict__)
        self.assertEqual(response.data['variables'], GetVariables())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_courses(self):
        # get API response
        response = self.client.get(reverse('course'))
        self.assertEqual(response.data['courses'], GetCourse())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_sosmed(self):
        # get API response
        response = self.client.get(reverse('social'))
        self.assertEqual(response.data['sosial_media'], GetSocialMedia())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_education(self):
        # get API response
        response = self.client.get(reverse('education'))
        self.assertEqual(response.data['educations'], GetEducation())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response_experience(self):
        # get API response
        response = self.client.get(reverse('experience'))
        self.assertEqual(response.data['experiences'], GetExperience())
        self.assertEqual(response.status_code, status.HTTP_200_OK)