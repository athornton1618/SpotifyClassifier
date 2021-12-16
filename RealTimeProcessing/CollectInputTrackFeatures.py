import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import numpy as np

os.environ['SPOTIPY_CLIENT_ID'] = '54453840737d4ec5812c403550b7a8c8'
os.environ['SPOTIPY_CLIENT_SECRET'] = '92f637c6155e4e568175acff3255c2c5'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

### PASS IN INPUT SONG_NAME FROM USER
song_name = 'All I Want for Christmas Is You'
###

results = sp.search(q='track:' + song_name, type='track')

#print(results)
with open("C:/Users/athor/Documents/git/SpotifyClassifier/data/junk.json", 'w') as f:
    json.dump(results, f, indent=4)

data = results["tracks"]["items"]
track = data[0]
track_id = track["id"]

print(track_id)

track_features = sp.audio_features(track_id)
track_features = track_features[0]
track_info = sp.track(track_id)
track_analysis = sp.audio_analysis(track_id)

track_features['popularity'] = track_info['popularity']
track_features['explicit'] = track_info['explicit']
album = track_info['album']
track_features['release_date'] = album['release_date']
track_features['release_date_precision'] = album['release_date_precision']

num_seg = 0
pitches = np.zeros(12)
timbre = np.zeros(12)

if "segments" in track_analysis:
    for _, j in enumerate(track_analysis['segments']):
        pitches += np.array(j['pitches'])
        timbre += np.array(j['timbre'])
        num_seg+=1

    track_features['avg_pitches'] = list(pitches/num_seg)
    track_features['avg_timbre'] = list(timbre/num_seg)
else:
    track_features['avg_pitches'] = list(pitches)
    track_features['avg_timbre'] = list(timbre)

print(track_features)
with open("C:/Users/athor/Documents/git/SpotifyClassifier/data/track_data.json", 'w') as f:
    json.dump(track_features, f, indent=4)

### CONVERT TRACK_FEATURES TO VECTORIZED FORM

### LOAD TRAINED MODEL

### CLASSIFY SONG

### SEND OUTPUT BACK TO FRONT END