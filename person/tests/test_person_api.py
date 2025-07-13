# import pytest
# from rest_framework.test import APIClient
# from django.contrib.auth.models import User

# @pytest.mark.django_db
# def test_authenticated_person_list():
#     # Setup: create user and get JWT token
#     user = User.objects.create_user(username='testuser', password='testpass')
#     client = APIClient()
#     token_response = client.post('/api/token/', {
#         "username": "testuser",
#         "password": "testpass"
#     })

#     assert token_response.status_code == 200
#     access_token = token_response.data['access']
#     client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

#     # Act: call the API endpoint
#     response = client.get('/api/person/')

#     # Assert: check the response is successful
#     assert response.status_code in [200, 204]
