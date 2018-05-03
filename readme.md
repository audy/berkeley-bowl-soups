# Berkeley Bowl Soup Scraper

Scraping soups from the Berkeley Bowl webpage and writing to an Sqlite
database

## Requirements

- Python 3
- R+tidyverse (for analysis)

## Analysis

See ![results](Rplots.pdf)

`make && open Rplots.pdf`

## Installation & Usage

`pip3 install -r requirements.txt`

## Docker

```sh
docker build --tag soups .

docker run \
  --rm \
  --volume \
  $PWD/soups.sqlite:/data/soups.sqlite \
  soups
```

With CRON:

```sh
# The website is updated randomly so I perform extra scrapes to make sure I
# catch all the soups
0 */4 * * * docker run --rm --volumes /root/soups/soups.sqlite:/data/soups.sqlite soups
```
