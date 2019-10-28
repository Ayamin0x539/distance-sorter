#!/usr/bin/env python

from __future__ import unicode_literals
import json
import os
import requests
import urllib

JSON_DATA_PATH='data.json'
API_KEY=os.environ['GOOGLE_MAPS_API_KEY']

def get_latitude_longitude(address):
    urlsafe_address = urllib.quote_plus(address)
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(urlsafe_address, API_KEY)
    
    response = requests.get(url)

    return response

def get_json_data():
    with open(JSON_DATA_PATH) as data_file:
        return json.load(data_file)

def main():
    data = get_json_data()

    test_location = data[0]['location']
    response = get_latitude_longitude(test_location)

    print('response: {} | {} |  {}'.format(response, response.status_code, response.content))

    for d in data:
        when = d['when']
        name = d['name']
        location = d['location']
        print('when: {} | name: {} | location: {}'.format(when,name,location))

if __name__=='__main__':
    main()
