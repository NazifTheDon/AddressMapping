import folium
import pandas as pd
import webbrowser
from main import extract_lang_long
import csv

#zoho_auth_url = "https://accounts.zoho.com/oauth/v2/auth?scope={scope}&client_id=1000.9JJW9BUVNQCHGM521QXVZXBEPF9R4J&response_type=code&access_type={offline or online}&redirect_uri={redirect_uri}&prompt=consent"

#places = {'cities': ["10915 Jasmine Crest Lane", "1600 Amphitheatre Parkway, Mountain View, CA"],
#          'latitude': [32.9165762, 37.4223878],
#          'longitude': [-117.1883953, -122.0841877],
#          'called': ['yes', 'no']}
#          #'visited': ['yes', 'yes']}


#df = pd.DataFrame(places, columns=['cities', 'latitude', 'longitude', 'called']).to_csv('places.csv')

address = pd.read_excel('Jolla 5 Primary Parcels.xlsx')

def marker_color(row):
    if row['called'] == 'yes':
        return 'green'
    #elif row['lived'] == 'no' and row ['visited'] == 'yes':
    #    return 'purple'
    return 'red'

#address['color'] = address.apply(marker_color, axis=1)

center = [47.116386, -101.299591]
map_USA = folium.Map(location=center, zoom_start=4)
for _, place in address.iterrows():
    if None not in extract_lang_long(place['MAIL_ADDRE']):
        location = extract_lang_long(place['MAIL_ADDRE'])
        folium.Marker(location, popup=f'{place["MAIL_NAME"]}', tooltip=place['MAIL_NAME'], icon=folium.Icon(prefix='fa', icon='circle')).add_to(map_USA)



# save map to html file
map_USA.save('index.html')
