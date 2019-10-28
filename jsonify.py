#!/usr/bin/env python

import json
import pprint

RAW_DATA_FILE='raw_data.txt'
NAME_PATTERN='Where: '
WHEN_PATTERN='When: '
LOCATION_PATTERN='Visit: '
SLICE_SIZE=4

def get_data_as_list_of_entries():
    '''
    Reads all data into memory, fine since data is small.
    Can be made more efficient using itertools.islice to produce a generator object.
    '''
    entries=[]
    
    with open(RAW_DATA_FILE) as raw_data:
        lines = [line for line in raw_data]
        i = 0
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue

        name = lines[i].strip()
        when = lines[i+1].strip()
        location = lines[i+2].strip()

        if not name.startswith(NAME_PATTERN) or \
           not when.startswith(WHEN_PATTERN) or \
           not location.startswith(LOCATION_PATTERN):
            raise ValueError('Incorrect format, unexpected patterns detected in name: [{}], when: [{}], and location: [{}].'.format(name, when, location))

        entry = {
            'name': lines[i].strip().replace(NAME_PATTERN, ''),
            'when': lines[i+1].strip().replace(WHEN_PATTERN, ''),
            'location': lines[i+2].strip().replace(LOCATION_PATTERN, '')
        }
        # the 4th line is empty
        i += SLICE_SIZE
        entries.append(entry)

    return entries

def main():
    data = get_data_as_list_of_entries()

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__=='__main__':
    main()
