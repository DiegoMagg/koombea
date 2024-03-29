from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login'), name='login-redirect'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('page/', include('page.urls')),
]
