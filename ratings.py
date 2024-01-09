import requests
from bs4 import BeautifulSoup
from user_info import FIDE_ID

def rating(event_type):
    URL = f"https://ratings.fide.com/profile/{FIDE_ID}"

    ratings = {
        "gray" : "Classic",
        "red"  : "Rapid",
        "blue" : "Blitz"
    }

    type_to_ratings = {
        "Klasika": "gray",
        "Rapid"  : "red" ,
        "Blitz"  : "blue"
    }


    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.findAll('div', attrs={'class':'col-lg-12 profile-top-rating-dataCont'}):
        rating = item.find('div', attrs={'class' : f'profile-top-rating-data profile-top-rating-data_{type_to_ratings[event_type]}'})
        return rating.text[6:].strip()

if __name__ == "__main__":
    print("Klasika:", rating("Klasika"))
    print("Rapid:", rating("Rapid"))
    print("Blitz:", rating("Blitz"))
