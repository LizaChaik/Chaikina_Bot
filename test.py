import requests
from random import randint
import bs4
array = []
id = 0
response = requests.get("https://zen.yandex.ru/id/5c014ebee79aa203d9ec6524")
soup = bs4.BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all('a', class_='card-image-compact-view__clickable')
print(quotes)
for quote in quotes:
    array.append(quote.get('href'))

rnd = randint(0, len(array))



