from bs4 import BeautifulSoup
import requests
import csv


html_text = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

# print(html_text)      # this is to see code is wrighting back to us in the terminal. 

souped_html = BeautifulSoup(html_text, 'lxml') 
movies = souped_html.find_all('h3', class_="title")


movie_names = [] # makes a list.



for name in movies: # this indexes and looks in that one area. 
    print(name.text.strip()) # this will run in the terminal with the list that we made.
    movie_names.append(name.text.strip()) # .append will add the movie names to to the list.




with open("movie_name.csv", "w", newline="", encoding="utf-8") as csvfile:  # We Import CSV to write names of movie into csv file for more readable
    writer = csv.writer(csvfile)
    writer.writerow(["Movie name"])
    for name in reversed(movie_names):
        writer.writerow([name])
 

#movie_names = []
                                                   # this is a bad try at making a list but we was on the right track.
# for movie in movie_names:
#   movie_names.append(movie.text.strip())