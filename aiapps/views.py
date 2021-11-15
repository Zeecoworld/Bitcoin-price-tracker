from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


# Create your views here.


def index(request):


    return render(request, "index.html")




def realtime(request):

    coin = "bitcoin"
    # url = 'https://www.google.com/search?q=' + (coin) + 'price'
    # # make a request to the website
    # HTML = requests.get(url)
    response = requests.get("https://www.google.com/search?q=" + coin + 'price')
    content = response.content
    # soup = BeautifulSoup()
    # soup = BeautifulSoup(content, 'html.parser')
    # parse the HTML
    soup = BeautifulSoup(content, 'html.parser')
    # find the current price
    price = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).text
    # return price
    # print(price)



    # price = get_latest_crypto_price('bitcoin')
    # print('BITCOIN price : ' + price)


    # return render(request, "index.html")
    return JsonResponse({"price": price})





def about(request):

    return render(request, "about.html")





def privacy(request):

    return render(request, "privacy.html")