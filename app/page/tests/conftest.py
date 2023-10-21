from http import HTTPStatus

import pytest
from requests.models import Response


@pytest.fixture
def crawler_data():
    return {
        'name': 'google.com',
        'links': [
            ['Link Text', 'https://google.com'],
        ],
    }


@pytest.fixture
def response_mock():
    response = Response()
    response._content = bytes()
    response.url = 'https://test.com'
    return response


@pytest.fixture
def request_get_mock(mocker):
    return mocker.patch('requests.get')


@pytest.fixture
def response_mock_ok(response_mock):
    response_mock.status_code = HTTPStatus.OK
    return response_mock
