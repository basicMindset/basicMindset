import requests
from bs4 import BeautifulSoup as bs4

def get_context():
	response = requests.get("https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/")
	if response.status_code != 200:
		print("Error fetching page")
		exit()
	else:
		content = response.content
	return content

print(get_context())