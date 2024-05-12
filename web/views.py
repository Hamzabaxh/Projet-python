from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    with open('data/phone.json', 'r') as f:
        data = json.load(f)

    with open('data/brand.json', 'r') as f:
        brands = json.load(f)

    selected_brand = request.GET.get('brand', None)
    min_price = request.GET.get('minPrice', None)
    max_price = request.GET.get('maxPrice', None)

    filtered_data = []
    for item in data:
        if selected_brand and item['marque'] != selected_brand:
            continue
        
        price = float(item['price'].replace(' TND', '').replace(',', '').strip())
        
        if min_price and price < float(min_price):
            continue
        
        if max_price and price > float(max_price):
            continue
        
        item['price'] = "{:.2f}".format(price) + ' DT'
        filtered_data.append(item)

    context = {
        'data': filtered_data,
        'brands': brands,
        'selected_brand': selected_brand,
        'selected_min_price': min_price,
        'selected_max_price': max_price,
    }
    return render(request, 'index.html', context)



