import requests
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager import chrome


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
		text: List[str] = [i.get_text() for i in page_soup.find_all('p') if len(i.get_text()) >= p_tag_min_length]
		if text != []:
			translate_text(text[0])
			break
		

def translate_text(text: str) -> str:
	browser: webdriver.PhantomJS = webdriver.PhantomJS(chrome.ChromeDriverManager.install(self='self'))
	browser.get('https://translate.google.com/?hl=es&sl=en&tl=es&text=hello%0Ahello%0Ahello&op=translate')
	html = browser.page_source
	google_translator_request: requests.Response = requests.get('https://translate.google.com/?hl=es&sl=en&tl=es&text=hello%0Ahello%0Ahello&op=translate')
	if not 200 <= google_translator_request.status_code <= 299:
		return ""
	google_translator_soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
	print(google_translator_soup.get_text())

