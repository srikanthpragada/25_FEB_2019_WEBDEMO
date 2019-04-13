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
        amount = request.GET['amount']
        rate = request.GET['disrate']
        if len(amount.strip()) == 0:
            message = "Amount is required!"
            return render(request, 'discount.html', {'message': message})
        elif len(rate.strip()) == 0:
            message = "Rate is required!"
            return render(request, 'discount.html', {'message': message})

        amount = float(amount)
        rate = float(rate)
        discount = amount * rate / 100;
        return render(request, 'discount.html',
                {'discount' : discount})
    else:
        return render(request, 'discount.html')



def calculate_discount_post(request):
    if request.method == "GET":
        return render(request,"discount_post.html")
    else:  # Post request, so process data
        amount = float(request.POST['amount'])
        rate = float(request.POST['disrate'])
        discount = amount * rate / 100;
        return render(request, 'discount_post.html',
                      {'discount': discount})

