import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

REDIRECT_URI = "http://example.com"
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
DATE = input('Enter date (YYYY-MM-DD): ')
URL = f"https://www.billboard.com/charts/hot-100/{DATE}" 


def get_songs(link):

    global DATE
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
    song_titles = [title.find(name="h3").text.split()[0] for title in divs]

    if not song_titles:
        DATE = input('Enter different date (YYYY-MM-DD): ')
        URL = f"https://www.billboard.com/charts/hot-100/{DATE}" 
        get_songs(URL)
    else:
        return song_titles
song_names = get_songs(link=URL)


#-----------------------------------------------------------------------------------


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, 
                                                client_secret=CLIENT_SECRET, 
                                                scope="playlist-modify-private", 
                                                redirect_uri=REDIRECT_URI, 
                                                show_dialog=False, 
                                                cache_path="./day_46_mixtape/cache.txt"))

song_uris = [sp.search(q=f"track:{name}", type="track")["tracks"]["items"][0]["uri"].split(":")[2] for name in song_names]

playlist = sp.user_playlist_create(user=sp.current_user()["id"], public=False, name=f"{DATE} top 100")

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
