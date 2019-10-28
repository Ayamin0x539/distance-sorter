# distance-sorter
Sort some locations by distance.

## Inspiration
What's the closest place I can get $1 oysters? I have the addresses but don't to plug them all into Google maps by hand. https://www.boston.com/food/restaurants/2019/07/16/dollar-oyster-deals-in-boston-cambridge-somerville

## Dependencies
- https://developers.google.com/maps/documentation/geocoding/start
- Python requests, geopy

## Usage
- Get a Google Maps API key, store it as a `GOOGLE_MAPS_API_KEY` environment variable. This project is set up to store it in a .env file, which can then be seeded using `source .env`.
- Run `jsonify.py`, which will parse the `raw_data.txt` into `data.json`.
- Run `transform_data_with_location_data.py`, which will add latitude and longitude data to the locations, leveraging Google Maps Geocoding API. This transforms `data.json` into `trasnformed_data.json`.
- Run `distance_sort.py --address <ADDRESS>` to generate a `sorted_locations.json` file, which sorts the locations by distance to the address provided as an argument.

## TODO
It says TODO, but I actually don't have time to do any of this. Feel free to open a pull request.
- Streamline all the scripts into a single call.
- Make input/output file names configurable.
- Maybe turn into a website for easier access. This was really just for me to find some cheap oysters.
- Currently just a naive geocode distance computation. Maybe expand to use actual pathing, taking traffic into account. On car or on foot.
