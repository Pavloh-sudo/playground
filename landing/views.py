from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import date

def home(request):
    today = date.today()
    return render(request, "landing/landing.html", {
        "name": "Pablo",
        "today": today,
        "age": 24
    })