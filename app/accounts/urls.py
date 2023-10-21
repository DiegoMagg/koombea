from accounts import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path(
        'login',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('register', views.RegisterView.as_view(), name='register'),
]
