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


# get playlist id for filters
filter_1_id = ''
filter_2_id = ''
filter_3_id = ''




for playlist in playlists['items']:
    if 'Playlist_filter_level_1' == playlist['name']:
        filter_1_id = playlist['id']
        
    if 'Playlist_filter_level_2' == playlist['name']:
        filter_2_id = playlist['id']

    if 'Playlist_filter_level_3' == playlist['name']:
        filter_3_id = playlist['id']

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


items_1 = sp.playlist_items(filter_1_id)['items']

items_2 = sp.playlist_items(filter_2_id)['items']

items_3 = sp.playlist_items(filter_3_id,)['items']

items_1_uris = []
for item in items_1:
    items_1_uris.append(item['track']['uri'])
items_2_uris = []
for item in items_2:
    items_2_uris.append(item['track']['uri'])
items_3_uris = []
for item in items_3:
    items_3_uris.append(item['track']['uri'])

# Add list 1 items to list 2 and list 3
for track_uri in items_1_uris:
    if track_uri not in items_2_uris:
        sp.playlist_add_items(filter_2_id, [track_uri])
    if track_uri not in items_3_uris:
        #sp.playlist_add_items(filter_3_id, [track_uri])
        pass

for track_uri in items_2_uris:
    if track_uri not in items_3_uris:
        #sp.playlist_add_items(filter_3_id, [track_uri])
        pass

print("done")


playlist_1 = sp.playlist(filter_1_id)
playlist_2 = sp.playlist(filter_2_id)
playlist_3 = sp.playlist(filter_3_id)


