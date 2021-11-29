import requests
import json

# Authentication + paths
token = input("Enter active Spotify API Token: ")

seed_genre = "hip-hop"
track_count = 750
track_url = 'https://api.spotify.com/v1/recommendations?' + 'seed_genres=' + seed_genre

data_path = "C:/Users/athor/Documents/git/SpotifyClassifier/Tracklists/"
data_file = seed_genre + ".json"
data_fullpath = data_path + data_file

# Construct Spotify API query
headers = {
    'Authorization': 'Bearer '+ token,
    'Content-type': 'application/json',
}

count = 0
tracks = {}
while count < track_count:
    # Query Spotify API
    try:
        response = requests.get(track_url, headers=headers).json()
    except:
        pass

    if "tracks" in response:
        for _, j in enumerate(response['tracks']):
            if not j['name'] in tracks: #Only add to tracklist if not seen before
                if count >= track_count:
                    break
                tracks[j['name']] = j['id']
                count+=1

    print(count)

with open(data_fullpath, 'w') as f:
   json.dump(tracks, f, indent=4)

