import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


# Create a user and log in for authenticated endpoints
@pytest.fixture
def create_admin_user(db):
    return User.objects.create_superuser(username='admin', email='admin@test.com', password='adminpass')


# Test home_page
@pytest.mark.django_db
def test_home_page(api_client):
    url = reverse('home_page')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "Hello from your Django Rest Api"


# Test test_db_connection
@pytest.mark.django_db
def test_db_connection(api_client):
    url = reverse('test_connection')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert 'Connection successful!' in response.json()


# Test register_user
@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse('register_user')

    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpass123'
    }

    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


# Test login_user
@pytest.mark.django_db
def test_login_user(api_client):
    url = reverse('login_user')
    User.objects.create_user(username='testuser', password='testpass123')

    data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK


# Test get_notes_by_user
@pytest.mark.django_db
def test_get_notes_by_user(api_client):
    user_id = 1
    url = reverse('get_notes_by_user', args=[user_id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


# Test get_notes_by_tag
@pytest.mark.django_db
def test_get_notes_by_tag(api_client):
    url = reverse('get_notes_by_tag', args=['test-tag'])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


# Test get_all_tags
@pytest.mark.django_db
def test_get_all_tags(api_client):
    user_id = 1
    url = reverse('get_all_tags', args=[user_id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


# Test get_user_by_username
@pytest.mark.django_db
def test_get_user_by_username(api_client):
    User.objects.create_user(username='testuser', password='testpass123')
    url = reverse('get_user_by_username', args=['testuser'])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
