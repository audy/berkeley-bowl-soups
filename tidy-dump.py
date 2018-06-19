#!/usr/bin/env python3

import berkeley_bowl
from itertools import groupby

import sys

db = berkeley_bowl.database()

soups_table = db['soups']

# unique by day and location
key = lambda r: (r['location_name'], r['timestamp'])

all_soups = set()

with open(sys.argv[2], 'w') as handle:

    handle.write('id,location_name,timestamp,soup\n')

    for record in soups_table:
        for soup in record['soups'].split(','):
            row = [
                record['id'],
                record['location_name'],
                record['timestamp'],
                soup.replace(',', ';').replace("\n", '')
            ]

            handle.write(','.join(str(i) for i in row))
            handle.write('\n')
