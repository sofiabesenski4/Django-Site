#normally would not put this logic in the django folder. Just to keep everything together
import bs4
import requests
def scrape_url(url_in):
    page= requests.get(url=url_in)
    return page