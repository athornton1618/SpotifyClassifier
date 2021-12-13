import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

seed_genres = ["alternative","indie","alt-rock","punk","grunge","punk-rock","indie-pop","emo","goth",\
    "hardcore","hardcore","death-metal","grindcore","black-metal","heavy-metal","metalcore","metal","metal-misc",\
    "dance","electronic","electro","edm","garage","house","chicago-house","breakbeat","dubstep","dance","techno","j-dance","deep-house",\
    "ambient","chill","sleep","new-age","study","piano",\
    "rock","rock-n-roll","rockabilly","j-rock","hard-rock","psych-rock","power-pop","guitar","drum-and-bass",\
    "country","bluegrass","acoustic","folk","honky-tonk",\
    "pop","k-pop","j-pop","cantopop","party","pop-film","r-n-n","club",\
    "jazz","soul","funk","blues","afrobeat",\
    "latin","latino","reggaeton","samba","salsa","bossanova",\
    "classical","opera"\
    "show-tunes","disney"]

track_count = 500

for genre in seed_genres:
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
        #response = sp.recommendations(seed_genres=[genre],limit=100)
        
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

        #print(count)
        

    with open(data_fullpath, 'w') as f:
        json.dump(tracks, f, indent=4)

    print("Completed Genre: " + genre + ", count: "+str(count))

