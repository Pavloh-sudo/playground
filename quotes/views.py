from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

days_of_week = {
    "monday": "Pienso, luego existo",
    "tuesday": "La vida es unn sueño",
    "wednesday": "El conocimiento es poder",
    "thursday": "Sé el cambio que quieres ver en el mundo",
    "friday": "Solo sé que no sé nada",
    "saturday": "Vive como si fuera el último día",
    "sunday": "Da un poco más todos los días"   
}


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound("No hay frase para este día")
    

def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El día no existe")
    redirect_day = days[day]
    return HttpResponseRedirect(f"/quotes/{redirect_day}")


def mont_of_the_year(request, month):

    months_dict = {
        "january": "Estamos en el mes de enero",
        "february": "Estamos en el mes de febrero",
        "march": "Estamos en el mes de marzo",
        "april": "Estamos en el mes de abril",
        "may": "Estamos en el mes de mayo",
        "june": "Estamos en el mes de junio",
        "july": "Estamos en el mes de julio",
        "august": "Estamos en el mes de agosto",
        "september": "Estamos en el mes de septiembre",
        "october": "Estamos en el mes de octubre",
        "november": "Estamos en el mes de noviembre",
        "december": "Estamos en el mes de diciembre"
    }

    month_lower = month.lower()

    quote_month = months_dict.get(month_lower, "Mes no válido o no encontrado")

    return HttpResponse(quote_month)



