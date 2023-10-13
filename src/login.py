import requests
import os

from bs4 import BeautifulSoup

from helper import LOGIN_URL


def fetch_csrf_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    token = soup.find('input', {'name': '_token'})['value']
    return token


def login(session:requests.Session):
    csrf_token = fetch_csrf_token(session, LOGIN_URL)
    
    payload = {
        'email': os.environ.get('FORUM_EMAIL'),
        'password': os.environ.get('FORUM_PASSWORD'),
        '_token': csrf_token
    }

    return session.post(LOGIN_URL, data=payload)


if __name__ == '__main__':
    with requests.Session() as session:
        print(login(session))