import requests

from bs4 import BeautifulSoup

url="https://www.empireonline.com/movies/features/best-movies-2/"


response= requests.get(url)

website_html=response.text

soup= BeautifulSoup(website_html, "html.parser")
all_movies=soup.find_all(name="h3", class_="title")

movies_title=[movie.getText() for movie in all_movies]
movies=movies_title[::-1]

with open('movie.txt', 'w') as file:

    for movie in movies:
        file.write(f"{movie}\n")  