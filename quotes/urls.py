
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index), 
    path("<int:day>", views.days_week_with_number), 
    path("<str:day>", views.days_week, name="day-quote"), 
    path("month/<str:month>", views.mont_of_the_year)
]