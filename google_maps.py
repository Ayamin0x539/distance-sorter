#!/usr/bin/env python

import requests
import os
import urllib

'''
A module for interfacing with google maps api.
'''

API_KEY=os.environ['GOOGLE_MAPS_API_KEY']

def get_latitude_longitude(address):
    urlsafe_address = urllib.quote_plus(address)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(urlsafe_address, API_KEY)

    response = requests.get(url)

    if not response.ok:
        return None
    
    json_response = response.json()

    location = json_response['results'][0]['geometry']['location']
    
    return location['lat'], location['lng']

