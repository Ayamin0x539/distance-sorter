#!/usr/bin/env python

from __future__ import unicode_literals
import json
import os
import requests
import urllib

JSON_DATA_PATH='data.json'
API_KEY=os.environ['GOOGLE_MAPS_API_KEY']
CITY_AND_STATE='Boston, MA'

def append_city_and_state(address):
    return address + ', ' + CITY_AND_STATE

def get_latitude_longitude(address):
    urlsafe_address = urllib.quote_plus(address)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(urlsafe_address, API_KEY)

    response = requests.get(url)
    json_response = response.json()

    location = json_response['results'][0]['geometry']['location']

    
    return location['lat'], location['lng']

def get_json_data():
    with open(JSON_DATA_PATH) as data_file:
        return json.load(data_file)

def transform_with_location(data):
    '''
    Transform json data for restaurants by adding latitude and longitude.
    '''

    transformed = []

    for d in data:
        when = d['when']
        name = d['name']
        location = d['location']

        location_with_city_and_state = append_city_and_state(location)
        latitude, longitude = get_latitude_longitude(location_with_city_and_state)
        print('when: {} | name: {} | location: {} | latitude: {} | longitude: {}'.format(when,name,location, latitude, longitude))

        # Don't destroy the input
        data = d.copy()
        data['latitude'] = latitude
        data['longitude'] = longitude
        
        transformed.append(data)

    return transformed



def main():
    data = get_json_data()
    transformed_data = transform_with_location(data)

    with open('transformed_data.json', 'w') as outfile:
        json.dump(transformed_data, outfile)
        

if __name__=='__main__':
    main()
