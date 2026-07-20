
from django.urls import path
from . import views

urlpatterns = [
    path("day/<int:day>", views.days_week_with_number), 
    path("day/<str:day>", views.days_week), #/quotes/monday/friday/etc
    path("month/<str:month>", views.mont_of_the_year)
]
