import requests

API_KEY = 'AIzaSyB6lqoeQ52EGo4Fm8MmlPhKoqTztZgiXRM'

address = 'Lublin, Węglin, ul. Koralowa'

params = {
    'key': API_KEY,
    'address': address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

response = requests.get(base_url, params=params)

# get longitude and latitude from response
response_data = response.json()
location = response_data['results'][0]['geometry']['location']

print(location)