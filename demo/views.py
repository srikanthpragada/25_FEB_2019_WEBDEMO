from datetime import datetime

import requests
from django.shortcuts import render


# Create your views here.

def welcome(request):
    # return HttpResponse("<h1>Django Demo</h1>")
    return render(request, 'welcome.html')


def shownow(request):
    now = datetime.now()
    return render(request, 'shownow.html', {"now": now})


def show_countries(request):
    try:
        resp = requests.get("https://restcountries.eu/rest/v2/all")
        if resp.status_code != 200:
            raise ValueError("Could not get details")

        countries = resp.json()
        return render(request, 'show_countries.html',
                      {"countries": countries,
                       "title": "List Of Countries"})
    except:
        return render(request, 'show_countries.html',
                      {"countries": None,
                       "title": "List Of Countries"})


def calculate_discount(request):
    if 'amount' in request.GET:
        print("Amount : ", request.GET['amount'])

    return render(request, 'discount.html')
