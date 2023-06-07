import os
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate_marketplace.settings')
django.setup()

from offers.models import Offers

API_KEY = 'AIzaSyB6lqoeQ52EGo4Fm8MmlPhKoqTztZgiXRM'
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

def get_location_from_google(address):
    params = {
        'key': API_KEY,
        'address': address
    }
    response = requests.get(base_url, params=params)
    response_data = response.json()
    location = response_data['results'][0]['geometry']['location']
    return location['lat'], location['lng']

def update_location():
    offers = Offers.objects.filter(latitude__isnull=True, longitude__isnull=True)

    for offer in offers:
        if offer.location:
            try:
                latitude, longitude = get_location_from_google(offer.location)
                offer.latitude = latitude
                offer.longitude = longitude
                offer.save()
                print(f'Updated latitude and longitude for offer id: {offer.id}')
            except:
                print(f'Error for offer id: {offer.id}')

if __name__ == '__main__':
    update_location()