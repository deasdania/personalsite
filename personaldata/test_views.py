import pytest

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def client():
    usert = User.objects.get(id=1)
    token = Token.objects.get(user=usert)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client

def test_path_get_variable(client):
    response = client.get(reverse('variable'))
    assert response.request['PATH_INFO'] == '/variable/'

def test_path_get_course(client):
    response = client.get(reverse('course'))
    assert response.request['PATH_INFO'] == '/course/'

def test_path_get_experience(client):
    response = client.get(reverse('experience'))
    assert response.request['PATH_INFO'] == '/experience/'

def test_path_get_education(client):
    response = client.get(reverse('education'))
    assert response.request['PATH_INFO'] == '/education/'

def test_path_get_social(client):
    response = client.get(reverse('social'))
    assert response.request['PATH_INFO'] == '/social/'

def test_path_get_about(client):
    response = client.get(reverse('about'))
    assert response.request['PATH_INFO'] == '/about/'

