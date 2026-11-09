from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", views.register, name="register"),
    path("", include("tracker.urls")),
]
