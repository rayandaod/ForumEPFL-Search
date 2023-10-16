import requests

from bs4 import BeautifulSoup
from tqdm import tqdm
from collections import defaultdict

from helper import *
from login import *


def get_page_companies(session:requests.Session, page_num:int, config:dict):
    url = config['companies_dir_url'].format(page_num)
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    company_links = defaultdict(dict)
    for row in soup.find_all('div', class_='directoryRow'):
        # Find company name
        name_div = row.find('div', class_='directoryRow__title')
        name = name_div.find('span', class_='font-h3').text
        print(name)

        # Find company link
        link = row.find('a', class_='directoryRow__link')['href']
        company_links[name]['link'] = link

        # Find company type (company, startup, or NGO/IGO)
        type_div = row.find('div', class_='directoryRow__badge')
        type_list = ['start-up', 'entreprise']  # although there are 3 company types, only 2 are actually used in the website source code
        _type_span, i = None, 0
        while _type_span is None:
            _type_span = type_div.find('span', class_=f'badge badge--{type_list[i]}')
            i += 1
        company_links[name]['type'] = _type_span.text.strip()

    return company_links


def get_all_companies(session:requests.Session, config:dict):
    company_links = {}
    for page_num in tqdm(range(1, config['num_pages']+1)):
        company_links.update(get_page_companies(session, page_num, config))
    return company_links


if __name__ == '__main__':
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    with requests.Session() as session:
        login(session, config['login_url'])
        save_to_json(get_all_companies(session, config))