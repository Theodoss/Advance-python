import requests 
from bs4 import BeautifulSoup


def main():
	url = "http://www.imdb.com/chart/top/"
	response = requests.get(url)
	# Response [200] = 正常連線
	print(response)
	html = response.text
	print(html)
	soup = BeautifulSoup(html,features="html.parser")
	tags = soup.find_all('td',{'class': 'titleColumn'})
	d ={}
	for i in tags:
		print(i.span.text)
		year = i.span.text
		if year not in d:
			d[year] = 1
		else:
			d[year] += 1
		print('__________________________________')
	for movie, count in sorted(d.items(),key= lambda t:t[1]):
		print(movie, '->',count)
if __name__ == '__main__':
	main()
