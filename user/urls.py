from django.urls import path

from user import views

urlpatterns = [
    path("whoami/", views.user_whoami),
    path("logout/", views.user_logout),
    path("login/", views.user_login),
]
