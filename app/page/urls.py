from django.urls import path
from page import views

urlpatterns = [
    path('', views.PageContentView.as_view(), name='page_data'),
    path('parse', views.page_parser_view, name='parse_page_data'),
    path('detail/<str:name>', views.PageDetailsView.as_view(), name='page_detail'),
]
