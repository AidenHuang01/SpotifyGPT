import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

username = '31yhl5xiqievgf7uqxovq2xfbmzu'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="2a407e6bd7524a4c830f7a854f86f516",
                                               client_secret="dff4b2d7889a48148022b9c31860b815",
                                               redirect_uri="https://localhost:8888/callback",
                                               scope="user-library-read, playlist-modify-private, playlist-read-private, playlist-modify-public user-library-modify"
                                               ))
playlists = sp.user_playlists(username)

print("logging: ", sys.argv[1])

msg = sys.argv[1]

playlist_id = ''
for playlist in playlists['items']:
    if "ChatGPT日推" == playlist['name']:
        playlist_id = playlist['id']

sp.playlist_change_details(playlist_id, description=msg)

