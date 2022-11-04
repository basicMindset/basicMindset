import requests, random
from bs4 import BeautifulSoup as soup

class getWordForGame():
	def __init__(self) -> None:
		self.url = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"

	def returnRandomWord(self):
		word = random.choice(self.parser(self.url)).upper()
		return word
	
	def parser(self, url):
		words = []
		context = soup(self.get_context(url), 'html.parser')
		for i in context.find_all(class_='row')[0]:
			for br in i.findAll('br'):
				next_s = br.nextSibling.lower()
				if len(next_s) > 4:
					words.append(next_s)
		return words

	def get_context(self, url):
		response = requests.get(url)
		if response.status_code != 200:
			print("Error fetching page")
			exit()
		else:
			content = response.text
		return content