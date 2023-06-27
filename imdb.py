from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.imdb.com/chart/top"
request = requests.get(url)

soup = BeautifulSoup(request.content, "lxml")
print(soup)
top_250_movie = soup.find("tbody", attrs={"class": "lister-list"}).find_all("tr")

film_order = 1
with open("film_list.txt", "w") as file:
    file.write("IMDB TOP 250\n")  
    for film in top_250_movie:
        name = film.find("td", attrs={"class": "titleColumn"}).a.text
        year = film.find("td", attrs={"class": "titleColumn"}).span.text
        point = film.find("td", attrs={"class": "ratingColumn imdbRating"}).strong.get("title")

        film_number = "film number: " + str(film_order)
        film_name = "film name: " + name
        film_year = "film year: " + year
        film_point = "film point: " + point
        print(film_number)
        file.write(film_number + "\n")  
        print(film_name)
        file.write(film_name + "\n")
        print(film_year)
        file.write(film_year + "\n")
        print(film_point)
        file.write(film_point + "\n")

        film_order = film_order + 1
