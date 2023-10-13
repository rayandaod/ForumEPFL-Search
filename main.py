import requests

from src.helper import save_to_json
from src.helper import COMPANY_LINKS_JSON_FILENAME, COMPANY_DETAILS_JSON_FILENAME
from src.login import *
from src.get_list import get_all_companies
from src.get_details import get_all_company_details


if __name__ == '__main__':
    with requests.Session() as session:
        login(session)
        save_to_json(get_all_companies(session), COMPANY_LINKS_JSON_FILENAME)
        save_to_json(get_all_company_details(session, COMPANY_LINKS_JSON_FILENAME), COMPANY_DETAILS_JSON_FILENAME)

