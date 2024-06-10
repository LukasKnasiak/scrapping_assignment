from bs4 import BeautifulSoup
import requests


html_text = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/ ").text

# print(html_text)      # this is to see code is wrighting back to us in the terminal. 

souped_html = BeautifulSoup(html_text, 'lxml')

movie_names = souped_html.find_all('h3')