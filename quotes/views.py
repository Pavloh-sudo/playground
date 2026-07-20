from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def quote(request):
    quote_day = [
        {"dia":"Lunes",
        "frase":"Pienso, luego existo"},
        {"dia":"Martes",
        "frase":"La vida es un sueño"},
        {"dia":"Miércoles",
        "frase":"El conocimiento es poder"},
        {"dia":"Jueves",
        "frase":"Sé el cambio que quieres ver en el mundo"},
        {"dia":"Viernes",
        "frase":"Solo sé, que no sé nada"},
        {"dia":"Sábado",
        "frase":"Vive como si fuera el último día"},
        {"dia":"Domingo",
        "frase":"Da un poco más todos los días"},
        ]
    return render(request, "quotes/landing.html", {
        "quote_day": quote_day
    })
    
def detail(request,day):
    HttpResponse(f'Frase del día {day}')

# def days_week(request, day):
#     try:
#         quote_text = days_of_week[day]
#         return HttpResponse(quote_text)
#     except KeyError:
#         return HttpResponseNotFound("No hay frase para este día")
    
    
# def index(request):
#     list_items = ""
#     days = list(days_of_week.keys())
    
#     for day in days:
#         day_path = reverse("day-quote", args=[day])
#         list_items += f"<li><a href='{day_path}'>{day}</a></li>"
        
#     response_html = f"<ul>{list_items}</ul>"
#     return HttpResponse(response_html)


# def days_week_with_number(request, day):
#     days = list(days_of_week.keys())
#     if day > len(days):
#         return HttpResponseNotFound("<h1>El día no existe</h1>")
#     redirect_day = days[day-1]
#     redirect_path = reverse("day-quote",args=[redirect_day])
#     return HttpResponseRedirect(redirect_path)
