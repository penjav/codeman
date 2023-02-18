from django.urls import path
from . import views


# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path("", views.nangchen, name="nangchen"),
#     path("_base/", views._base, name="base"),
#     path("about/", views.about, name="about"),
#     path("contact/", views.contact, name="contact"),
#     path("history/", views.history, name="history"),
# ] + static(settings.STATIC_URL, ducument_root=settings.STATIC_ROOT)

urlpatterns = [
    path("", views.nangchen, name="nangchen"),
    path("_base/", views._base, name="base"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("history/", views.history, name="history"),
]
