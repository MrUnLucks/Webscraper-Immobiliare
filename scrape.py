import requests
from bs4 import BeautifulSoup
import csv

data = []
filename = 'data.csv'

def write_to_file():
    # Write data to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = data[0].keys()
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        csvwriter.writerows(data)

def read_csv_as_dicts(filename):
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return list(csv_reader)
    
def compare_ids():
    csvOld = read_csv_as_dicts('data.csv')

    # Extract all IDs from both lists
    ids_old = {row['ID'] for row in csvOld}

    # Filter items in csv that are not in csvOld
    new_items = [item for item in data if item['ID'] not in ids_old]
    return new_items
    

def scrape_website(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    isPage = soup.find('div', class_='in-errorMessage__bg')
    if(isPage is not None):
        print(isPage)
        return
    # number_of_elements =len(soup.find_all('li',class_='in-searchLayoutListItem'))
    cards = soup.find_all('div', class_='in-listingCardPropertyContent')
    for card in cards:
        titleTag = card.find('a', class_='in-listingCardTitle')
        link = titleTag.get('href')
        id =  link.split("/")[-2]
        title = titleTag.get('title')
        price = card.find('div', class_='in-listingCardPrice')
        isArredato = card.find(lambda tag: tag.name == 'use' and tag['xlink:href'] == '#couch-lamp')
        items = card.find_all('div', class_='in-listingCardFeatureList__item')
        locals = '0'
        size = '0'
        for item in items:
            if(item.find(lambda tag: tag.name == 'use' and tag['xlink:href'] == '#planimetry')):
               locals = item.find('span').get_text().replace('locali', "")
            if(item.find(lambda tag: tag.name == 'use' and tag['xlink:href'] == '#size')):
                size = item.find('span').get_text().replace('m²', "")
        data.append({'ID':id,"Link":link,"Title": title,"Price":price.text.replace('€',''),"Locali":locals,"Metratura":size,"isArredato": bool(isArredato)})


def scrape_immobiliare():
    pages_to_scrape = 5
    for i in range(pages_to_scrape):
        scrape_website(f'https://www.immobiliare.it/affitto-case/padova-provincia/?criterio=rilevanza&prezzoMassimo=900&localiMinimo=3&pag={i}')
    differentItems = compare_ids()
    print(differentItems)
    write_to_file()
    return differentItems

scrape_immobiliare()