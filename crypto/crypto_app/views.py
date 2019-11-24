from django.shortcuts import render

def home(request):
    import requests
    import json
    #Price API
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,LTC,XLM,ADA,USDT,MIOTA,TRX,EOS,XRP&tsyms=CAD")
    price = json.loads(price_request.content)


    #News API
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    if request.method == "POST":
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=CAD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto':crypto})
    else:
        notfound = "Enter a crypto symbol into the search bar"
        return render(request, 'prices.html', {'notfound': notfound})