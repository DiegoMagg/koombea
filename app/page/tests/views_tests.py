from http import HTTPStatus

import pytest
from django.urls import reverse
from model_bakery import baker

pytestmark = pytest.mark.django_db


def test_crawler_must_redirect_if_form_is_invalid(authed_client, request_get_mock):
    response = authed_client.post(reverse('parse_page_data'))
    assert response.status_code == HTTPStatus.FOUND


def test_scrapped_itens_must_return_into_the_initial_page(authed_client, activated_user):
    queryset = baker.make('page.PageContent', user=activated_user, links=[['Test', 'https://test.com']])
    response = authed_client.get(reverse('page_data'))
    assert response.status_code == HTTPStatus.OK
    assert queryset.name in response.content.decode('UTF-8')
    assert str(queryset.total_links) in response.content.decode('UTF-8')


def test_page_must_return_details_of_page(authed_client, activated_user):
    queryset = baker.make('page.PageContent', user=activated_user, links=[['Test', 'https://test.com']])
    response = authed_client.get(reverse('page_detail', kwargs={'name': queryset.name}))
    page_content = response.content.decode('UTF-8')
    assert response.status_code == HTTPStatus.OK
    assert queryset.name in page_content
    assert queryset.links[0][1] in page_content
