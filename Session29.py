import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

tags = soup.find_all("td", class_="titleColumn")
rates=soup.find_all("td",class_="ratingColumn imdbRating")

movies = []
years = []
rating=[]

for tag in tags:
    # print(tag.text)
    movieTitle = tag.text.strip()
    movies.append(movieTitle)
    # print("----------")

for rateTag in rates:
    ratings=float(rateTag.text.strip())
    rating.append(ratings)

print(rating)
for movie in movies:
    print(movie)
    print("~~~~~~~~~~~")

