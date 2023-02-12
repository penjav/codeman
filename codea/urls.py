from django.urls import path
from . import views

urlpatterns = [
    path("", views.nangchen, name="nangchen"),
    path("_base/", views._base, name="base"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("history/", views.history, name="history"),
]