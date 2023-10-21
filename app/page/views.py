from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from page.crawlers import page_links_crawler
from page.forms import UrlParserForm
from page.models import PageContent


class PageContentView(LoginRequiredMixin, ListView):
    paginate_by = 6
    model = PageContent
    template_name = 'page_content.html'

    def get_queryset(self):
        return PageContent.objects.filter(user=self.request.user)


class PageDetailsView(LoginRequiredMixin, View):
    template_name = 'page_detail.html'

    def get(self, request, name):
        queryset = get_object_or_404(PageContent, user=request.user, name=name)
        return render(request, self.template_name, locals())


async def page_parser_view(request):
    form = UrlParserForm(data=request.POST)
    if not form.is_valid():
        return redirect(reverse('page_data'))
    queryset, _ = await PageContent.objects.aget_or_create(user=request.user, **form.cleaned_data)
    await page_links_crawler(request, form.cleaned_data['url'], queryset)
    return redirect(reverse('page_data'))
