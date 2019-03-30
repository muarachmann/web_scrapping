from bs4 import BeautifulSoup
import requests

page = requests.get("https://developers.google.com/open-source/gsoc/timeline")

soup = BeautifulSoup(page.content, 'html.parser')

trs = soup.find_all('tr')

print(trs)
