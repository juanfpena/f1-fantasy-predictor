import requests

def html_getter(url: str) -> str:
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return {'success': True, 'content': response.content}
    
    return {'success': False, 'content': response.status_code}