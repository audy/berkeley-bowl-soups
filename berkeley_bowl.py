import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import dataset


def database():
    db_path = sys.argv[1]
    print("connecting to db {}".format(db_path))
    db = dataset.connect("sqlite:///{}".format(db_path))

    return db


def locations():
    """
    Scrape soups list of Berkeley Bowl's webpage.
    """

    res = requests.get("https://www.berkeleybowl.com/", headers={"User-Agent": "Soup Scraper"})

    soup = BeautifulSoup(res.content, "html.parser")

    home_soups = soup.find_all("section", id="home-soups")[0]

    time_string = home_soups.find("strong").text
    timestamp = datetime.strptime(time_string, "%m/%d/%Y")

    locations = home_soups.find_all("div", class_="col-md-3")

    for location in locations:

        location_name = location.find("h2", class_="grn").text

        soups = [li.text for li in location.find("ul", class_="soup-list").find_all("li")]

        yield {"name": location_name, "timestamp": timestamp, "soups": soups}
