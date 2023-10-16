import json
import requests
import yaml


def save_to_html(data:str, html_filename:str='index.html') -> None:
    with open(html_filename, 'wb') as f:
        f.write(data)

def save_to_json(data:dict, json_filename:str) -> None:
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    with open('./config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    with requests.Session() as session:
        from login import login
        login(session, config['login_url'])
        save_to_html(session.get(config['companies_dir_url'].format(1)).content, './output/index.html')