import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from user_info import FIDE_ID

URL = f"https://ratings.fide.com/profile/{FIDE_ID}"

ratings = {
    "gray" : "Classic",
    "red"  : "Rapid",
    "blue" : "Blitz"
}

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

for item in soup.findAll('div', attrs={'class':'col-lg-12 profile-top-rating-dataCont'}):
    for key in ratings:
        rating = item.find('div', attrs={'class' : f'profile-top-rating-data profile-top-rating-data_{key}'})
        print(ratings[key], rating.text[6:].strip())
