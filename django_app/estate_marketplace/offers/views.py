from django.core.serializers import serialize
from django.http import JsonResponse
from .models import Offers
from django.shortcuts import render

def get_offers_data(request):
    offers = Offers.objects.all()
    geojson= {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type":"Point",
                    "coordinates":[float(offer.longitude), float(offer.latitude)],
                },
                "properties": {
                    "title": offer.title,
                    "price": offer.price,
                    "area" : offer.footer,
                    "price_per_meter": int(offer.price / offer.footer) if (offer.price and offer.footer) else None,
                    "location": offer.location,
                    "link": offer.url,
                },
            }
            for offer in offers if offer.longitude and offer.latitude
        ],
    }
    return JsonResponse(geojson)

def view_map(request):
    return render(request, 'offers/map.html')
 