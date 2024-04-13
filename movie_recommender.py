import requests 
from bs4 import BeautifulSoup
import random

movie_url = "https://www.imdb.com/chart/top/"
response = requests.get(movie_url)

if response.status_code == 200:
    print("Successful")
else:
    print("Error",response.status_code)
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
movies = soup.find_all('tr', class_='titleRow')

movie_data = []
for movie in movies:
    title = movie.find('td', class_='titleColumn').a.text.strip()
    genre = movie.find('span', class_='genre').text.strip()
    rating = float(movie.find('strong').text.strip())
    movie_data.append({'title': title, 'genre': genre, 'rating': rating})

genre_pref = input("Enter your preferred genre (or leave blank for any): ").strip()
min_rating = float(input("Enter the minimum rating you'd like (0.0 to 10.0): ").strip())

def recommend_movie(movies, genre_pref, min_rating):
    filtered_movies = [movie for movie in movies if (genre_pref in movie['genre'] or not genre_pref) and movie['rating'] >= min_rating]
    if filtered_movies: 
        return random.choice(filtered_movies)
    else:
        return "No movies found based on your preferences."

recommendation = recommend_movie(movie_data, genre_pref, min_rating)
print("We recommend:", recommendation)
