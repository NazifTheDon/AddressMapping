from urllib.parse import urlencode
import requests
import pandas as pd

with open('API_credentials') as f:
    api_key = f.readline()

df = pd.read_excel('Jolla 5 Primary Parcels.xlsx')
address = df['MAIL_ADDRE']
#print(address)

#"1600 Amphitheatre Parkway, Mountain View, CA"

def extract_lang_long(address_or_postalcode, data_type  = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    parameters = {"address": address_or_postalcode, "key": api_key}
    url_parameters = urlencode(parameters)
    url = f"{endpoint}?{url_parameters}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    lat_long = {}
    try:
        lat_long = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return [lat_long.get('lat'), lat_long.get('lng')]

for x in address:
    print(x)
    print(extract_lang_long(x))

#address = input("What's the address dawg ")
#print(extract_lang_long(address))
