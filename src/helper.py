import json

LOGIN_URL = 'https://platform.forumepfl.ch/login'
COMPANIES_DIR_URL = 'https://platform.forumepfl.ch/edition/5/student/6965/companies?page={}'  # TODO: get latest edition number automatically
NUM_PAGES = 36  # TODO: get number of pages automatically

COMPANY_LINKS_JSON_FILENAME = './output/output1_list.json'
COMPANY_DETAILS_JSON_FILENAME = './output/output2_details.json'


def save_to_html(data:str, html_filename:str='index.html') -> None:
    with open(html_filename, 'wb') as f:
        f.write(data)

def save_to_json(data:dict, json_filename:str) -> None:
    with open(json_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)