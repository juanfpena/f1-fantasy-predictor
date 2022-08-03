from bs4 import BeautifulSoup
from scripts.html_getter import html_getter
import warnings
import json
import requests

warnings.filterwarnings('ignore')

json_file = open('data/config.json')
loaded_json = json.load(json_file)

# api documentation @ https://documenter.getpostman.com/view/11462073/TzY68Dsi

if __name__ == '__main__':
    
    drivers = loaded_json['drivers']
    constructors = loaded_json['constructors']
    
    cookie_json = {"solution":{"interrogation":{"st":162229509,"sr":1959639815,"cr":78830557},"version":"stable"},"error":'',"performance":{"interrogation":185}}
    cookie_headers = {'d': 'account.formula1.com'}
    
    cookie = requests.post('https://api.formula1.com/6657193977244c13', headers=cookie_headers, json=cookie_json)
    

    