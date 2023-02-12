from django.urls import path
from . import views

urlpatterns = [
    path("", views.nangchen, name="nangchen"),
    path("about/", views.about, name="about"),
]
