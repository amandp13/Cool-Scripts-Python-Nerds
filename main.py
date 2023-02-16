import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL="https://www.billboard.com/charts/hot-100/"

date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

list=[]

response =requests.get(f"{URL}{date}/")
web_html=response.text
soup=BeautifulSoup(web_html,"html.parser")
data=soup.select(selector="li ul li h3")
for song in data:
    list.append(song.text.strip('\n\t'))
print(list)

SPOTIPY_CLIENT_ID= "08fe757b2fa3430284e4846308b58bac"
SPOTIPY_CLIENT_SECRET = "232b810d7f5a4e178293aa7806449806"
SURL = "https://api.spotify.com/v1/users/user_id/playlists"
SPOTIPY_REDIRECT_URI="http://localhost:8888/callback/"
OAUTH_TOKEN_URL= 'https://accounts.spotify.com/api/token'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,redirect_uri=SPOTIPY_REDIRECT_URI,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,show_dialog=True,cache_path="token.txt"))
user_id=sp.current_user()["id"]
song_uris=[]
year=date.split("-")[0]
for song in list:
    result=sp.search(q=f"track:{song} year:{year}",type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesnt excist in spotify,skipped.")
playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billiboard 100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)