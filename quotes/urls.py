
from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.quote, name="quote"), 
    # path("<int:day>", views.days_week_with_number), 
    # path("<str:day>", views.days_week, name="day-quote"), 
    path("detail/", views.detail,name="detail"),
]