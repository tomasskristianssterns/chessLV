import os, shutil
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from datetime import date
from openpyxl import Workbook
from user_info import PATH


URL = "https://www.sahafederacija.lv/kalendars/"
TODAY = str(date.today())
CURRENT_DAY = int(TODAY.replace("-", ""))

def download():
    workbook = Workbook()
    worksheet=workbook.active

    worksheet['A1'].value = "Date"
    worksheet['B1'].value = "Tournament name"
    worksheet['C1'].value = "Regulation name"
    worksheet['D1'].value = "Email"
    worksheet['E1'].value = "Type"

    #If there is no such folder, the script will create one automatically
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    else:
        shutil.rmtree(PATH)
        os.mkdir(PATH)

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    i = 2

    for item in soup.findAll('div', attrs={'class' : 'single-kalendar-article'}):
        links = item.select("a[href$='.pdf']")

        if not links:
            continue

        tournament_name = item.find('a')

        for link in links:

            number = item.find('span', attrs={'class' : 'small-text'})
            tournament_date_string = number.string.strip().replace(" ","").replace("\n","")

            tournament_date_string = tournament_date_string.strip()
            tournament_date_result = tournament_date_string.replace(".","").replace("-","").replace(" ","")
            tournament_date = tournament_date_result[4:8]+tournament_date_result[2:4]+tournament_date_result[0:2]
            tournament_date = int(tournament_date)

            if(tournament_date < CURRENT_DAY):
                break

            worksheet['A' + str(i)] = tournament_date_string
            worksheet['B' + str(i)] = tournament_name.string

            #Name the pdf files using the last portion of each link which are unique in this case
            filename = os.path.join(PATH,"tournament"+str(i-1)+".pdf")
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(URL,link['href'])).content)
                worksheet['C' + str(i)] = filename

        if(tournament_date < CURRENT_DAY):
            break

        i += 1

    workbook.save('tournaments.xlsx')
    workbook.close()

if __name__ == "__main__":
    download()