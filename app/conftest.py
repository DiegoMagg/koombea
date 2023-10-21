import pytest
from django.test import Client
from model_bakery import baker


@pytest.fixture
def user_data():
    return {
        'username': 'username',
        'password': '%x3oRGsv7NYTMd',
    }


@pytest.fixture
def user(user_data):
    user = baker.make('accounts.User', username=user_data['username'])
    user.set_password(user_data['password'])
    return user


@pytest.fixture
def activated_user(user):
    user.is_active = True
    user.save()
    user.refresh_from_db()
    return user


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def authed_client(activated_user):
    client = Client()
    client.force_login(activated_user)
    return client
