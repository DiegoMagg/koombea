import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from page.models import PageContent


def select_anchors_starting_with_http(bs):
    return [[i.text, i['href']] for i in bs.find_all('a', string=True) if i['href'].startswith('http')]


async def page_links_crawler(request, url: str, page_content: PageContent):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        bs = BeautifulSoup(response.content, 'html.parser')
        title_element = bs.find('title')
        page_content.name = title_element.text if title_element else ''
        page_content.links = select_anchors_starting_with_http(bs)
        page_content.status = PageContent.SUCCESS
    except Exception as e:
        messages.warning(request, e)
        await page_content.adelete()
        return
    await page_content.asave()
    return page_content
