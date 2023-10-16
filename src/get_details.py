import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

from helper import *
from login import *


def get_details_from_link(session:requests.Session, company:dict):
    response = session.get(company['link'])
    soup = BeautifulSoup(response.content, 'html.parser')

    info = {}

    # Extract company description after <span class="font-h3">Description</span>
    # or after <h2 class="prestation__title">Company Profile</h2>
    # There can be several p and we want all until the next h2 or font-h3 tag
    description = ''
    description_started = False
    for tag in soup.find_all():
        if (tag.name == 'span' and tag.get('class') == ['font-h3'] and tag.text == 'Description') or \
            (tag.name == 'h2' and tag.get('class') == ['prestation__title'] and tag.text == 'Company Profile'):
                description_started = True
        elif description_started:
            if tag.name == 'p':
                description += tag.text
            elif tag.name == 'h2' or tag.name == 'span' or tag.name == 'font-h3':
                break
    info['description'] = description
    # print(description)

    # Extract company Employment offers after <span class="font-h3">Employment offers</span>
    # There can be several p and we want all until the next h2 or font-h3 tag
    employment_offers = ''
    employment_offers_started = False
    for tag in soup.find_all():
        if tag.name == 'span' and tag.get('class') == ['font-h3'] and tag.text == 'Employment offers':
            employment_offers_started = True
        elif employment_offers_started:
            if tag.name == 'p':
                employment_offers += tag.text
            elif tag.name == 'h2' or tag.name == 'span' or tag.name == 'font-h3':
                break
    info['employment_offers'] = employment_offers
    # print(employment_offers)

    # Extract company Required profiles
    # There can be several p and we want all until the next h2 or font-h3 tag
    required_profiles = ''
    required_profiles_started = False
    for tag in soup.find_all():
        if tag.name == 'span' and tag.get('class') == ['font-h3'] and tag.text == 'Required profiles':
            required_profiles_started = True
        elif required_profiles_started:
            if tag.name == 'p':
                required_profiles += tag.text
            elif tag.name == 'h2' or tag.name == 'span' or tag.name == 'font-h3':
                break
    info['required_profiles'] = required_profiles
    # print(required_profiles)

    return info


def get_all_company_details(session:requests.Session, company_list_path:str, stop:int=None):
    with open(company_list_path) as json_file:
        company_list = json.load(json_file)

    company_details = company_list
    for i, company_name in enumerate(tqdm(company_list.keys())):
        print(company_name)
        company_details[company_name].update(get_details_from_link(session, company_list[company_name]))
        if stop is not None and i == stop:
            break
    
    return company_details


if __name__ == '__main__':
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    with requests.Session() as session:
        login(session, config['login_url'])
        company_details = get_all_company_details(session, config['company_list_path'])
        save_to_json(company_details, config['company_details_path'])
