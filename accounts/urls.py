from django.urls import path
from .views import dashboard, profile,home

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("",home, name="home"),
]