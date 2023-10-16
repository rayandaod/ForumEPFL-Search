import requests
import os
import yaml

from bs4 import BeautifulSoup
from helper import save_to_html


def fetch_csrf_token(session:requests.Session, url:str):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    token = soup.find('input', {'name': '_token'})['value']
    return token


def login(session:requests.Session, login_url:str):
    csrf_token = fetch_csrf_token(session, login_url)
    
    payload = {
        'email': os.environ.get('FORUM_EMAIL'),
        'password': os.environ.get('FORUM_PASSWORD'),
        '_token': csrf_token
    }

    return session.post(login_url, data=payload)


if __name__ == '__main__':
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    with requests.Session() as session:
        save_to_html(login(session, config['login_url']).content, './output/login_resp.html')