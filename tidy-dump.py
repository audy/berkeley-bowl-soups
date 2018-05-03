#!/usr/bin/env python3

import berkeley_bowl
from itertools import groupby

db = berkeley_bowl.database()

soups_table = db['soups']

# unique by day and location
key = lambda r: (r['location_name'], r['timestamp'])

all_soups = set()

print('id,location_name,timestamp,soup')

for record in soups_table:
    for soup in record['soups'].split(','):
        row = [
            record['id'],
            record['location_name'],
            record['timestamp'],
            soup.replace(',', ';').replace("\n", '')
        ]

        print(','.join(str(i) for i in row))
