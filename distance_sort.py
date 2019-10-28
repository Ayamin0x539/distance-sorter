#!/usr/bin/env python

from __future__ import unicode_literals
import argparse
import geopy.distance
import json

from google_maps import get_latitude_longitude

TRANSFORMED_JSON_DATA_PATH='transformed_data.json'

def get_transformed_data():
    '''
    Returns a list of dicts, where each dict has keys (name, when, location, latitude, longitude)
    '''
    with open(TRANSFORMED_JSON_DATA_PATH) as data_file:
        return json.load(data_file)

def get_distance_in_miles(latitude_from, longitude_from, latitude_to, longitude_to):
    '''
    Computes the distance between two lat/longs, using the vincenty distance from geopy (more accurate ellipsoidal models than Haversine formula. Haversine assumed the earth is a sphere, which results in errors up to 0.5% ;)
    See https://stackoverflow.com/questions/38248046/is-the-haversine-formula-or-the-vincentys-formula-better-for-calculating-distan
    '''
    return geopy.distance.vincenty((latitude_from, longitude_from), (latitude_to, longitude_to)).mi
    

def transform_data_with_distances(locations, origin_location):
    '''
    Transforms imported data by adding a `distance` entry to each map, indicating the distance in miles from the origin_location.
    '''
    transformed_data = []
    for location in locations:
        distance_in_miles = get_distance_in_miles(origin_location['latitude'], origin_location['longitude'], location['latitude'], location['longitude'])
        copied_data = location.copy()
        copied_data['distance'] = distance_in_miles

        transformed_data.append(copied_data)

    return transformed_data
    
def sort_by_distance_between(locations, origin_location):
    '''
    Sorts location data by distance to origin_location.
    location : dict() with keys (name, where, location, latitude, longitude).
    origin_location : dict() with keys (latitude, longitude)
    '''

    data_with_distances = transform_data_with_distances(locations, origin_location)

    return sorted(data_with_distances, key = lambda entry: entry['distance'])

def parse_address_from_args():
    '''
    Extract the address from args. This will be used to determine origin location.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', nargs='+', required=True)

    arguments = parser.parse_args()

    return ' '.join(arguments.address)

def main():
    address = parse_address_from_args()

    origin_latitude, origin_longitude = get_latitude_longitude(address)
    
    locations = get_transformed_data()

    origin_location = {'latitude': origin_latitude, 'longitude': origin_longitude}

    sorted_locations = sort_by_distance_between(locations, origin_location)

    with open('sorted_locations.json', 'w') as outfile:
        json.dump(sorted_locations, outfile)

if __name__=='__main__':
    main()
