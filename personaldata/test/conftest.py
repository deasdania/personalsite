import pytest
from personalsite import settings
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'db.example.com',
        'NAME': 'external_db',
    }

@pytest.fixture
def api_client():
    user = User.objects.get(id=1)
    token = Token.objects.get(user=user)
    client = APIClient().credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client

