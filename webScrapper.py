from bs4.element import ResultSet
import requests
from bs4 import BeautifulSoup


def test() -> None:
    request: requests.Response = requests.get('https://www.google.com/search?q=que+es+arduino')
    soup: BeautifulSoup = BeautifulSoup(request.text, 'html.parser')
    notUsefullSites: str = ['youtube.com', 'support.google.com', 'accounts.google.com']
    for a in soup.find_all('a'):
        if not a.has_attr('href') or ('/url?q=' not in a.get('href') or any(item in a.get('href') for item in notUsefullSites)):
            continue
        link: str = a.get('href')
        link = link.split('/url?q=')[1]
        link = link.split('&')[0]
        print()
        print(link)
