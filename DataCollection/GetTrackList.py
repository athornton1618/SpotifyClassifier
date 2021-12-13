import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

genre = "show-tunes"
track_count = 500

data_path = "C:/Users/athor/Documents/git/SpotifyClassifier/TracklistsFull/"
data_file = genre + ".json"
data_fullpath = data_path + data_file

count = 0
nothing_new = 0
tracks = {}
#Break if reached desired number tracks OR no unique tracks seen in X iterations
while count < track_count and nothing_new<20:
    # Query Spotify API
    try:
        response = sp.recommendations(seed_genres=[genre],limit=100)
    except:
        pass
    
    new_count=0
    if "tracks" in response:
        for _, j in enumerate(response['tracks']):
            if not j['name'] in tracks: #Only add to tracklist if not seen before
                if count >= track_count:
                    break
                tracks[j['name']] = j['id']
                new_count+=1
                count+=1
                nothing_new = 0

    if new_count == 0:
        nothing_new+=1

    print(count)

with open(data_fullpath, 'w') as f:
   json.dump(tracks, f, indent=4)

