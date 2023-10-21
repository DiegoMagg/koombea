from http import HTTPStatus

import pytest
from asgiref.sync import async_to_sync
from django.test.client import RequestFactory
from django.urls import reverse
from model_bakery import baker
from page.crawlers import page_links_crawler
from page.models import PageContent

pytestmark = pytest.mark.django_db


def test_crawler_must_retrieve_anchors(request_get_mock, response_mock_ok):
    response_mock_ok._content = str.encode(
        '<title>Test</title>'
        '<a href="https://externalurl.com">External Url</a>'
    )
    request_get_mock.return_value = response_mock_ok
    request = RequestFactory()
    queryset = baker.make(PageContent)
    assert queryset.links is None
    async_to_sync(page_links_crawler)(request, 'http://domain.test', queryset)
    assert PageContent.objects.exists() is True


def test_crawler_must_raise_errors_and_delete_page_content_instance(request_get_mock, response_mock, mocker):
    mocker.patch('django.contrib.messages.warning')
    response_mock.status_code = HTTPStatus.UNAUTHORIZED
    request_get_mock.return_value = response_mock
    request = RequestFactory()
    queryset = baker.make(PageContent)
    assert PageContent.objects.exists() is True
    async_to_sync(page_links_crawler)(request, 'http://domain.test', queryset)
    assert PageContent.objects.exists() is False
