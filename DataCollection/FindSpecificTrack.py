import requests
import json

# Authentication + paths
token = input("Enter active Spotify API Token: ")

song_name = 'All I Want for Christmas Is You'
artist = 'Mariah Carey'

url = 'https://api.spotify.com/v1/search?q=track:' + song_name + '%20artist:' + artist + '&type=track'

# Construct Spotify API query
headers = {
    'Authorization': 'Bearer '+ token,
    'Content-type': 'application/json',
}

# Query Spotify API
response = requests.get(url, headers=headers).json()
print(response)