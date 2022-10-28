import requests, random
from bs4 import BeautifulSoup as soup

class getWordForGame():
	def __init__(self, url) -> None:
		self.url = url

	def chooseRandom(self):
		return random.choice(self.parser(self.url))
	
	def parser(self, url):
		words = []
		context = soup(self.get_context(url), 'html.parser')
		for i in context.find_all(class_='row')[0]:
			for br in i.findAll('br'):
				next_s = br.nextSibling.lower()
				if len(next_s) > 4:
					words.append(next_s)
		return words

	@staticmethod
	def get_context(url):
		response = requests.get(url)
		if response.status_code != 200:
			print("Error fetching page")
			exit()
		else:
			content = response.text
		return content