from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from datetime import date

def home(request):
    today = date.today()
    stack = ['Python','Django','Golang','PHP','JS']
    return render(request, "landing/landing.html", {
        "name": "Fernando",
        "today": today,
        "age": 24,
        "stack": stack
    })