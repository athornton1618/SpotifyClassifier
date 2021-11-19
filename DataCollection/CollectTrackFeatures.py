import requests
import json

# Authentication + paths
token = input("Enter active Spotify API Token: ")

track_id = '2TpxZ7JUBn3uw46aR7qd6V'
track_url = 'https://api.spotify.com/v1/audio-features/' + track_id

data_path = "C:/Users/athor/Documents/git/SpotifyClassifier/data/"
data_file = "track_1.json"
data_fullpath = data_path + data_file

# Construct Spotify API query
headers = {
    'Authorization': 'Bearer '+ token,
    'Content-type': 'application/json',
}

# Query Spotify API
response = requests.get(track_url, headers=headers).json()
#print(response)

# Save data
with open(data_fullpath, 'w') as f:
    json.dump(response, f)