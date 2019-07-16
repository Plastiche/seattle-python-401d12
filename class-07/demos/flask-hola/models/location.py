from os import environ
import json
import requests

class Location:
    
    def __init__(self, search_query, info):
        self.search_query = search_query
        self.formatted_query = info['formatted_address']
        self.latitude = info['geometry']['location']['lat'];
        self.longitude = info['geometry']['location']['lng'];  

    def serialize(self):
        return vars(self)

    @staticmethod
    def fetch(query):
        """
        Fetches gecode data for a given location query
        returns as json
        """

        api_key = environ.get('GEOCODE_API_KEY')

        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}'

        locations = requests.get(url).json()

        location = Location(query, locations['results'][0])

        return json.dumps(location.serialize())
