import requests
import os

API_KEY = os.environ["MOVIE_API_KEY"]
POSTER_URL = "https://image.tmdb.org/t/p/original"
URL = "https://api.themoviedb.org/3/search/movie"
DATA = ""


def find_movie(title):
    MOVIE = title
    global DATA
    
    parameters = {"query": MOVIE, "api_key": API_KEY}

    response = requests.get(URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    DATA = data

    return {f"{i['original_title']} - {i['release_date']}":i['id'] for i in data["results"]}


def selected_movie_data(id):
     for movie in DATA['results']:
       if movie['id'] == id:
            return {"title":f"{movie['original_title']}", "year":f"{movie['release_date'].split('-')[0]}", "description":f"{movie['overview']}", "image":f"{POSTER_URL}{movie['poster_path']}"}
        


