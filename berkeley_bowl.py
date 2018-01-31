import requests
from bs4 import BeautifulSoup
from datetime import datetime


def locations():
    '''
    Scrape soups list of Berkeley Bowl's webpage.
    '''

    url = 'http://www.berkeleybowl.com/daily-hot-soup'

    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html5lib')

    locations = soup.find_all('div', class_='block-inner')[3:5]

    for location in locations:

        location_name = location.find(class_='block-title').text

        time_string = location.find_all(class_='field-item')[0].text
        timestamp = datetime.strptime(time_string, '%A, %B %d, %Y - %I:%M')

        # parse timestamp

        soups = [ n.text for n in location.find_all(class_='field-item')[1:] ]

        yield {
            'name': location_name,
            'timestamp': timestamp,
            'soups': soups
            }
