import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from person.models import Person
from uuid import uuid4
from datetime import datetime


@pytest.fixture
def auth_client(db):
    """Returns an authenticated APIClient instance."""
    user = User.objects.create_user(username='testuser', password='testpass')
    client = APIClient()
    response = client.post('/api/token/', {
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    access_token = response.data['access']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    return client

