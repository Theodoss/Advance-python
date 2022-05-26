"""
File: web_crawler_avg.py
Name:
--------------------------
This file demonstrates how to get
averages on www.imdb.com/chart/top
Do you know the average score of 250 movies?
Let's use Python code to find out the answer
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('td', {'class','ratingColumn imdbRating'})
	print(tags)
	d ={}
	num = 0
	val = 0
	for tag in tags:
		val += float(tag.text)
		num += 1

	print(val/num)

	#########################
	#                       #
	#         TODO:         #
	#                       #
	#########################


if __name__ == '__main__':
	main()
