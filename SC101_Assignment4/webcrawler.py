"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():

    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

    # ----- Write your code below this line ----- #
        boy_count = 0
        girl_count = 0
        lines = soup.table.tbody

        for line in lines:
            line = line.get_text()

            line = line.split()
            if len(line) == 5:
                boy_num = line[2].replace(',', '')
                girl_num = line[4].replace(',', '')
                boy_count += int(boy_num)
                girl_count += int(girl_num)
        print(f'Male Number: {boy_count}')
        print(f'Female Number: {girl_count}')




if __name__ == '__main__':
    main()
