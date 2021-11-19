import requests
import json
import simplejson

# Authentication + paths
token = input("Enter active Spotify API Token: ")

track_id = '0bYg9bo50gSsH3LtXe2SQn' # Track: All I Want for Christmas Is You
track_url = 'https://api.spotify.com/v1/audio-features/' + track_id

data_path = "C:/Users/athor/Documents/git/SpotifyClassifier/data/"
data_file = "all_i_want_for_christmas_is_you.json"
data_fullpath = data_path + data_file

# Construct Spotify API query
headers = {
    'Authorization': 'Bearer '+ token,
    'Content-type': 'application/json',
}

# Query Spotify API
response = requests.get(track_url, headers=headers).json()
#print(response)

# Dump data, (not human readable))
with open(data_fullpath, 'w') as f:
   json.dump(response, f, indent=4)