import spotipy
from spotipy.oauth2 import SpotifyOAuth



class SpotifyGPT:
    def __init__(self, username, client_id, client_secret) -> None:
        """
        SpotifyGPT query body
        """
        self.sp = None
        self.playlists = []
        self.username = username
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                    client_secret=client_secret,
                                                    redirect_uri="https://localhost:8888/callback",
                                                    scope="user-library-read, playlist-modify-private, playlist-read-private, playlist-modify-public user-library-modify"
                                                    ))
        self.playlists = self.sp.user_playlists(username)

    def get_playlist_id_by_name(self, playlist_name):
        for playlist in self.playlists['items']:
            if playlist['name'] == playlist_name:
                return playlist['id']
        return ''

    def get_playlist_tracks(self, playlist_id):
        results = self.sp.user_playlist_tracks(self.username,playlist_id)
        tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        return tracks

    

    
