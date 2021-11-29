import requests
import json

# Authentication + paths
token = input("Enter active Spotify API Token: ")
track_url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'

# Construct Spotify API query
headers = {
    'Authorization': 'Bearer '+ token,
    'Content-type': 'application/json',
}

# Query Spotify API
response = requests.get(track_url, headers=headers).json()
print(response)

# Dump data, (not human readable))
with open("genres.json", 'w') as f:
   json.dump(response, f, indent=4)