from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("snippet/", views.snippet_details, name="snippet_details")
]