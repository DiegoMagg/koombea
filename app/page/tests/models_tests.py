import pytest
from page.models import PageContent

pytestmark = pytest.mark.django_db


def test_page_content_model_instance_must_be_created(activated_user, crawler_data):
    total_urls_in_page = len(crawler_data['links'])
    qs = PageContent.objects.create(user=activated_user, **crawler_data)
    assert qs.links == crawler_data['links']
    assert qs.total_links == total_urls_in_page
    assert qs.__str__() == crawler_data['name']
