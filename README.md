# distance-sorter
Sort some locations by distance.

## Inspiration
What's the closest place I can get $1 oysters? I have the addresses but don't to plug them all into Google maps by hand. https://www.boston.com/food/restaurants/2019/07/16/dollar-oyster-deals-in-boston-cambridge-somerville

## Dependencies
- https://developers.google.com/maps/documentation/geocoding/start

## Start
Get a Google Maps API key, store it as a `GOOGLE_MAPS_API_KEY` environment variable. This project is set up to store it in a .env file, which can then be seeded using `source .env`.

The raw data file was parsed using `jsonify.py`.

## TODO
- Maybe turn into a website for easier access. This was really just for me to find some cheap oysters.
- Currently just a naive geocode distance computation. Maybe expand to use actual pathing, taking traffic into account. On car or on foot.
