import requests
import json
import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

#id = '0bYg9bo50gSsH3LtXe2SQn'
id = '2rd9ETlulTbz6BYZcdvIE1'
response = sp.track(id)

#print(response)

popularity = response['popularity']
explicit = response['explicit']
album = response['album']
release_date = album['release_date']
release_date_precision = album['release_date_precision']

#print(popularity)
#print(explicit)
#print(release_date)
#print(release_date_precision)

response = sp.audio_analysis(id)

num_seg = 0
loudness_max = 0
pitches = np.zeros(12)
timbre = np.zeros(12)

track = response['track']
time_signature = track['time_signature']
key = track['key']
mode = track['mode']

if "segments" in response:
    for _, j in enumerate(response['segments']):
        loudness_max = max(loudness_max,j['loudness_max'])
        pitches += np.array(j['pitches'])
        timbre += np.array(j['timbre'])
        num_seg+=1

pitches = pitches/num_seg
timbre = timbre/num_seg

print(loudness_max)
print(pitches)
print(timbre)
print(time_signature)
print(key)
print(mode)

#with open("C:/Users/athor/Documents/git/Sandbox/test.json", 'w') as f:
#    json.dump(response, f, indent=4)
