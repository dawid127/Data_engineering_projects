import requests
import csv
from datetime import datetime
import time
from bs4 import BeautifulSoup

# adres strony z danymi o cenach paliw
url = 'https://www.orlen.pl/PL/DlaBiznesu/HurtoweCenyPaliw/Strony/default.aspx'

# nagłówki żądania HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# plik, w którym będą zapisywane dane (save file)
filename = 'ceny_paliw.csv'

# funkcja do pobierania danych ze strony i zapisywania ich do pliku
def scrape_prices():
    # pobranie strony
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # wybór tabeli z danymi o cenach paliw
    table = soup.find('table', {'class': 'ms-rteTable-6'})
    
    # inicjalizacja listy wierszy do zapisu w pliku
    rows = []
    
    # iteracja po wierszach tabeli
    for tr in table.find_all('tr')[1:]:
        # wybór komórek z danymi
        tds = tr.find_all('td')
        name = tds[0].text.strip()
        current_price = float(tds[1].text.strip().replace(',', '.'))
        previous_price = float(tds[2].text.strip().replace(',', '.'))
        price_diff = current_price - previous_price
        
        # dodanie wiersza do listy
        rows.append([name, current_price, previous_price, price_diff, datetime.now()])
    
    # zapisanie danych do pliku CSV
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# pętla nieskończona, w której co 10 minut uruchamiana jest funkcja scrape_prices()
while True:
    scrape_prices()
    time.sleep(600)  # 10 minut
