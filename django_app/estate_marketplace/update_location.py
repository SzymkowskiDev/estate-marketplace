'''
First attempt to update latitude and longitude for offers. It updated only half of the offers. Better solution is to use Google API -> update_location2.py
'''
import os 
import django
from geopy.geocoders import Nominatim

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate_marketplace.settings')
django.setup()

from offers.models import Offers

def update_location():
    geolocator = Nominatim(user_agent="offers")
    offers = Offers.objects.filter(latitude__isnull=True, longitude__isnull=True)

    for offer in offers:
        if offer.location:
            location = geolocator.geocode(offer.location, timeout=10)
        if location:
            offer.latitude = location.latitude
            offer.longitude = location.longitude
            offer.save()
            print(f'Updated latitude and longitude for offer id: {offer.id}')

if __name__ == '__main__':
    update_location()