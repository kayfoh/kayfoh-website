from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.webpages, name="webpages"),
    path("portfolio_page", views.portfolio_page, name="portfolio_page"),
    path("vacations_page", views.vacations_page, name="vacations_page")
]