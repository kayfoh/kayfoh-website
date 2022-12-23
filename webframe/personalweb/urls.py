from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact_page, name="contact"),
    path("about", views.about_page, name="about"),
    path("<str:name>", views.webpages, name="webpages")
]