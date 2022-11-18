import folium
import pandas as pd
import webbrowser
from main import extract_lang_long
import csv

class Map:
    def __init__(self, location, zoom_start):
        self.location = location
        self.zoom_start = zoom_start

    def showMap(self):
        # Create the map
        my_map = folium.Map(location=self.location, zoom_start=self.zoom_start)

        # Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")

places = {'cities': ["10915 Jasmine Crest Lane", "1600 Amphitheatre Parkway, Mountain View, CA"],
          'latitude': [32.9165762, 37.4223878],
          'longitude': [-117.1883953, -122.0841877]}


df = pd.DataFrame(places, columns=['cities', 'latitude', 'longitude']).to_csv('places.csv')

address = pd.read_csv('places.csv')
print(address.head())
center = [47.116386, -101.299591]
map_USA = folium.Map(location=center, zoom_start=3)
for index, place in address.iterrows():
    location = [place['latitude'], place['longitude']]
    folium.Marker(location, popup = f'Address: {place["cities"]}').add_to(map_USA)

# save map to html file
map_USA.save('index.html')