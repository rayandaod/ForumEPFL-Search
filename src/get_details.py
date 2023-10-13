import requests

from bs4 import BeautifulSoup
from tqdm import tqdm

from helper import *
from login import *


def get_details_from_link(session:requests.Session, company_link:str):
    response = session.get(company_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    save_to_html(response.content)

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


def get_all_company_details(session:requests.Session, company_list_json:str):
    with open(company_list_json) as json_file:
        company_links = json.load(json_file)

    company_details = {}
    for company_name, company_link in tqdm(company_links.items()):
        company_details[company_name] = get_details_from_link(session, company_link)
    
    return company_details


if __name__ == '__main__':
    with requests.Session() as session:
        login(session)
        save_to_json(get_all_company_details(session, COMPANY_LINKS_JSON_FILENAME), COMPANY_DETAILS_JSON_FILENAME)