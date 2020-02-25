from bs4 import BeautifulSoup
import requests

filename = "ssd.csv"
f = open(filename, "w")

headers = "title, product, rating, price\n"

f.write(headers)

source = requests.get('https://www.newegg.com/p/pl?N=100011693%204814%20600038463&page=1').text

soup = BeautifulSoup(source, 'lxml')


for i in range(int(soup.find('span', class_='list-tool-pagination-text').strong.text.split('/')[1])):
	print(i)
	currSource = requests.get('https://www.newegg.com/p/pl?N=100011693%204814%20600038463&page=' + str(i))
	item = BeautifulSoup(currSource.text, 'lxml')

	for item in soup.find_all('div', class_='item-container'):

		img_src = item.find('a', class_='item-img')['href']

		title = item.find('a', class_='item-title').text
		print(title)

		rating = item.find('a', class_='item-rating')
		if (rating != None):
			rating = rating['title']
			rating = rating[-1:]

		price_src = item.find('li', class_='price-current').text
		price = price_src.split("\n")[2]
		price = price.split("\xa0")[0]
		price = price[1:]
		price = price.replace(",","")

		if (rating != None):
			f.write(title.replace(",","|") + "," + img_src + "," + rating + "," + price + "\n")
		else:
			f.write(title.replace(",","|") + "," + img_src + "," + "NULL" + "," + price + "\n")

f.close()