from bs4 import BeautifulSoup
from scripts.html_getter import html_getter
import warnings

warnings.filterwarnings('ignore')

if __name__ == '__main__':
    url = 'https://www.f1fantasytracker.com/drivers-teams.html'

    response = html_getter(url)
    
    if response['success']:
        
        soup = BeautifulSoup(response['content'], 'html.parser')
        
        a_array = soup.findAll('a')
        
        refs = []
        
        for tag in a_array:
            
            test_string = str(tag).split('"')
            
            for string in test_string:
                if ".html" in string:
                    refs.append(string)
        
        relevant_refs = refs[8:-7]
        split = url.split('drivers-teams.html')
        base_url = ''.join(split)
        
        for ref in [relevant_refs[0]]:
            
            player_url = f'https://www.f1fantasytracker.com/{ref}'
            
            response = html_getter(player_url)
            
            if response['success']:
                
                soup = BeautifulSoup(response['content'], 'html.parser')
                
                print(soup.prettify())
        
        
    else:
        
        print(response['content'])

    