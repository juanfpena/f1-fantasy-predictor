from bs4 import BeautifulSoup
from scripts.html_getter import html_getter
import warnings
import json

warnings.filterwarnings('ignore')

json_file = open('data/config.json')
loaded_json = json.load(json_file)

if __name__ == '__main__':
    
    drivers = loaded_json['drivers']
    constructors = loaded_json['constructors']
    
    for driver in drivers:
        player_url = f'https://www.f1fantasytracker.com/{driver}'
        response = html_getter(player_url)
    
        if response['success']:
            
            soup = BeautifulSoup(response['content'], 'html.parser')
            
            for i in range(0,24):
                print(soup.findAll(id=f'Total{i}'))
            
            break
            
        
        
    else:
        
        print(response['content'])

    