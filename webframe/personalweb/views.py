from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Welcome!")

def portfolio_page(request):
    return HttpResponse("Welcome to my portfolios page")

def vacations_page(request):
    return HttpResponse("Welcome to the Vacations page")

def webpages(request, name):
    return HttpResponse(f"Welcome to the {name}")
