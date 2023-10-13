import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

from helper import *
from login import *


def get_page_companies(session:requests.Session, page_num):
    url = COMPANIES_DIR_URL.format(page_num)
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    company_links = {}
    for row in soup.find_all('div', class_='directoryRow'):
        title_div = row.find('div', class_='directoryRow__title')
        title = title_div.find('span', class_='font-h3').text
        link = row.find('a', class_='directoryRow__link')['href']
        company_links[title] = link

    return company_links


def get_all_companies(session:requests.Session):
    company_links = {}
    for page_num in tqdm(range(1, NUM_PAGES+1)):
        company_links.update(get_page_companies(session, page_num))
    return company_links


if __name__ == '__main__':
    with requests.Session() as session:
        login(session)
        save_to_json(get_all_companies(session), COMPANY_LINKS_JSON_FILENAME)