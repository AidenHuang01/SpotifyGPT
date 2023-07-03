# Shows a user's playlists (need to be authenticated via oauth)

import spotipy
from spotipy.oauth2 import SpotifyOAuth




username = '31yhl5xiqievgf7uqxovq2xfbmzu'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="2a407e6bd7524a4c830f7a854f86f516",
                                               client_secret="dff4b2d7889a48148022b9c31860b815",
                                               redirect_uri="https://localhost:8888/callback",
                                               scope="user-library-read, playlist-modify-private, playlist-read-private, playlist-modify-public user-library-modify"
                                               ))

playlists = sp.user_playlists(username)


playlist_id = ''
for playlist in playlists['items']:
    if 'AWS_Communicate_Test' == playlist['name']:
        playlist_id = playlist['id']
        break

track_id = 'spotify:track:04x6DpeFQ72efXsD0DmWPQ'
sp.playlist_add_items(playlist_id, [track_id])
