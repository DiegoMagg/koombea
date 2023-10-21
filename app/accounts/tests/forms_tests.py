import pytest
from accounts.forms import RegisterForm
from accounts.models import User

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize('key', ['username', 'password'])
def test_register_form_should_raise_error_if_field_is_missing(key, user_data):
    user_data[key] = None
    form = RegisterForm(user_data)
    assert form.is_valid() is False
    field_error = form.errors.get(key)
    assert field_error is not None


def test_register_form_should_raise_error_if_username_is_already_registered(user_data, activated_user):
    expected_error = {'username': ['This username is already being used.']}
    form = RegisterForm(user_data)
    assert form.is_valid() is False
    assert form.errors == expected_error


def test_register_form_should_be_valid(user_data):
    form = RegisterForm(user_data)
    assert form.is_valid() is True


def test_register_form_should_create_user(user_data):
    assert User.objects.exists() is False
    form = RegisterForm(user_data)
    assert form.is_valid() is True
    user = form.save()
    user.check_password(form.cleaned_data['password'])
    assert User.objects.exists() is True
