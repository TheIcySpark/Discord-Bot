import requests
from typing import Dict, List
from bs4 import BeautifulSoup


def get_links(google_search_query: str) -> List[str]:
	google_search_request: requests.Response = requests.get('https://www.google.com/search?q=' + google_search_query)
	google_search_soup: BeautifulSoup = BeautifulSoup(google_search_request.text, 'html.parser')
	sites_to_exclude: str = ['youtube.com', 'support.google.com', 'accounts.google.com', 'www.google.com/preferences']

	return [a_tag.get('href').split('/url?q=')[1].split('&')[0] for a_tag in google_search_soup.find_all('a') 
			if (a_tag.has_attr('href') and '/url?q=' in a_tag.get('href') and not any(i in a_tag.get('href') for i in sites_to_exclude))]


def gahter_information(links: List[str], p_tag_min_length: int = 250) -> List[Dict]:
	information_from_pages: List[Dict] = []
	for link in links:
		try:
			page_request: requests.Response = requests.get(link)
		except requests.exceptions.ConnectionError:
			continue
		if not 200 <= page_request.status_code <= 299:
			continue
		page_soup: BeautifulSoup = BeautifulSoup(page_request.text, 'html.parser')
		paragraphs: List[str] = [i.get_text() for i in page_soup.find_all('p') if (len(i.get_text()) >= p_tag_min_length <= 1999)]
		if paragraphs != []:
			information_from_pages.append({'paragraphs': paragraphs, 'link': link})
	return information_from_pages