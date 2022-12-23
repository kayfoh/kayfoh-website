from django.http import HttpResponse
from django.shortcuts import render

import datetime

tasks = ["foo", "bar", "zoo"]

# Create your views here.
def index(request):
    return render(request, "homepage/index.html")

def contact_page(request):
    return render(request, "homepage/contact.html")

def about_page(request):
    return render(request, "homepage/about.html")

def webpages(request, name):
    timenow = datetime.datetime.now()
    return render(request, "homepage/webpages.html", {
        "name": name.capitalize(),
        "timeofday": timenow.hour < 18,
        "tasks":tasks
    })
