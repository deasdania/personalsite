from django.test import TestCase, Client
from .models import AboutDesc, Variable
from .serializers import VariableSerializer
from pytest_django.asserts import assertTemplateUsed
# Create your tests here.

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

# Include an appropriate `Authorization:` header on all requests.



def test_create(self):
    response = self.client.get(reverse('create', args=[self.userName]))
    self.assertEqual(response.status_code, 200)


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

    def test_get_variables(self):
        # get API response
        response = self.client.get(reverse('variable'))
        # print(response.__dict__)
        # get data from db
        variables = Variable.objects.all()
        variablelist = []

        for variable in variables:
            variabledict = {}
            variabledict["id"] = variable.id
            variabledict["name"] = variable.name
            variabledict["value"] = variable.value
            variablelist.append(variabledict)
        self.assertEqual(response.data['variables'], variablelist)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_path_get_variable(self):
        # get API response
        response = self.client.get(reverse('variable'))
        self.assertEqual(response.request['PATH_INFO'], '/variable/')

    def test_path_get_course(self):
        # get API response
        response = self.client.get(reverse('course'))
        self.assertEqual(response.request['PATH_INFO'], '/course/')

    def test_path_get_experience(self):
        # get API response
        response = self.client.get(reverse('experience'))
        self.assertEqual(response.request['PATH_INFO'], '/experience/')

    def test_path_get_education(self):
        # get API response
        response = self.client.get(reverse('education'))
        self.assertEqual(response.request['PATH_INFO'], '/education/')

    def test_path_get_social(self):
        # get API response
        response = self.client.get(reverse('social'))
        self.assertEqual(response.request['PATH_INFO'], '/social/')

    def test_path_get_about(self):
        # get API response
        response = self.client.get(reverse('about'))
        self.assertEqual(response.request['PATH_INFO'], '/about/')