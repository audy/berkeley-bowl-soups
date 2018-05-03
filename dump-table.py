#!/usr/bin/env python3

import berkeley_bowl
from itertools import groupby

db = berkeley_bowl.database()

soups_table = db['soups']

# unique by day and location
key = lambda r: (r['location_name'], r['timestamp'])


all_soups = set()

for row in soups_table:
    for soup in row['soups'].split(','):
        all_soups.add(soup)

all_soups = sorted(list(all_soups))
with open('/dev/stdout', 'w') as handle:

    #handle.write(','.join(all_soups))
    #handle.write("\n")

    for grp, items in groupby(sorted(soups_table, key=key), key=key):
        items = list(items)
        item = items[0]

        days_soups = set(item['soups'].split(','))

        for soup in all_soups:
            if soup in days_soups:
                handle.write('#')
            else:
                handle.write(' ')
        handle.write("\n")

