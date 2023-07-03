import time
from datetime import datetime
from datetime import date
from pytz import timezone    
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
    if "ChatGPT日推Legacy" == playlist['name']:
        playlist_id = playlist['id']

def runSync():
    with open("demo.py") as f:
        exec(f.read())

def runRecommend():
    with open("recommend.py") as f:
        exec(f.read(), globals())

def runLog(msg):
    sp.playlist_change_details(playlist_id, description=msg)
    print(msg)

def composeMsg(sync_success, sync_fail, recommand_success, recommand_fail, tick):
    msg = ""
    msg += datetime.now(timezone("America/Los_Angeles")).strftime("%Y/%m/%d %H:%M:%S") + " "
    msg += compseDuration(tick)
    msg += "sync_success:" + str(sync_success) + " "
    msg += "sync_fail:" + str(sync_fail) + " "
    msg += "recommand_success:" + str(recommand_success) + " "
    msg += "recommand_fail:" + str(recommand_fail)
    return msg

def compseDuration(tick):
    day = 0
    hour = 0
    minute = 0
    tick_num = tick
    day = tick_num // (60 * 60 * 24)
    tick_num = tick_num % (60 * 60 * 24)
    hour = tick_num // (60 * 60)
    tick_num = tick_num % (60 * 60)
    minute = tick_num // (60)
    msg = "Duration: "
    if day != 0:
        msg += str(day) + "D "
    if hour != 0:
        msg += str(hour) + "H "
    if minute != 0:
        msg += str(minute) + "Min "
    return msg

tick = 0
sync_success = 0
sync_fail = 0
recommand_success = 0
recommand_fail = 0
while True:
    if tick % 300 == 0:
        try:
            runSync()
        except:
            sync_fail += 1
        else:
            sync_success += 1

    if tick % 14400 == 0:
        try:
            runRecommend()
        except:
            recommand_fail += 1
        else:
            recommand_success += 1

    msg = composeMsg(sync_success, sync_fail, recommand_success, recommand_fail, tick)
    runLog(msg)
    tick += 60
    time.sleep(60)
