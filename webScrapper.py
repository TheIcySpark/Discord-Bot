import requests
import goslate
from typing import List
from bs4 import BeautifulSoup


def get_links(google_search_query: str) -> List[str]:
	google_search_request: requests.Response = requests.get('https://www.google.com/search?q=' + google_search_query)
	google_search_soup: BeautifulSoup = BeautifulSoup(google_search_request.text, 'html.parser')
	sites_to_exclude: str = ['youtube.com', 'support.google.com', 'accounts.google.com', 'www.google.com/preferences']

	return [a_tag.get('href').split('/url?q=')[1].split('&')[0] for a_tag in google_search_soup.find_all('a') 
			if (a_tag.has_attr('href') and '/url?q=' in a_tag.get('href') and not any(i in a_tag.get('href') for i in sites_to_exclude))]


def gahter_information(links: List[str], p_tag_min_length: int = 225) -> None:
	for link in links:
		try:
			page_request: requests.Response = requests.get(link)
		except requests.exceptions.ConnectionError:
			continue
		if not 200 <= page_request.status_code <= 299:
			continue
		page_soup: BeautifulSoup = BeautifulSoup(page_request.text, 'html.parser')
		paragraphs: List[str] = [i.get_text() for i in page_soup.find_all('p') if len(i.get_text()) >= p_tag_min_length]
		if paragraphs != []:
			summarize_paragraphs(paragraphs)
			break


def summarize_paragraphs(paragraphs: str) -> List[str]:
	new_paragraphs: List[str] = []
	for paragraph in paragraphs:
		print(paragraph)
		new_paragraphs.append(summarize_paragraph(paragraph))
		break
	return new_paragraphs


def summarize_paragraph(paragraph: str) -> str:
	translator = goslate.Goslate()
	# languaje_id = translator.detect(paragraph)
	# languaje_description = translator.get_languages()[languaje_id]
	# print(languaje_description)

	print(translator.translate('hello', 'de'))