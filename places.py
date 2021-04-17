import googlemaps
import pprint
import webbrowser
from API_KEY import API_KEY

API_KEY = API_KEY

client = googlemaps.Client(key=API_KEY)

def open_map():
    location_result = client.find_place(input="221 Baker Street, London UK", input_type="textquery")

    for place in location_result['candidates']:
        place_id = place['place_id']
        my_fields = ['url']
        place_detail = client.place(place_id=place_id, fields=my_fields)

        pprint.pprint(place_detail['result']['url'])

    link = place_detail['result']['url']
    webbrowser.open(url=link)