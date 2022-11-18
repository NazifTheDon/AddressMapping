from urllib.parse import urlencode
import requests
import csv
import pandas as pd
import folium
franchises = pd.read_csv('places.csv')
#view the dataset
print(franchises.head())
center = [-0.023559, 37.9061928]
map_kenya = folium.Map(location=center, zoom_start=8)
for index, franchise in franchises.iterrows():
    location = [franchise['latitude'], franchise['longitude']]
    folium.Marker(location, popup = f'Name:').add_to(map_kenya)

# save map to html file
map_kenya.save('index.html')

with open('API_credentials') as f:
    api_key = f.readline()

#"1600 Amphitheatre Parkway, Mountain View, CA"


def extract_lang_long(address_or_postalcode, data_type  = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    parameters = {"address": address_or_postalcode, "key": api_key}
    url_parameters = urlencode(parameters)
    url = f"{endpoint}?{url_parameters}"
    r = requests.get(url)
    if r.status_code not in range (200, 299):
        return {}
    lat_long = {}
    try:
        lat_long = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return [lat_long.get('lat'), lat_long.get('lng')]



#address = input("What's the address dawg ")
#print(extract_lang_long("10915 Jasmine Crest Lane"))
