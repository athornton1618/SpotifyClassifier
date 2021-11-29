import requests
import json

# Authentication + paths
token = input("Enter active Spotify API Token: ")

seed_genres = ["ambient","alternative","anime","blues","classical","country","death-metal","dubstep",\
                "electronic","folk","gospel","goth","grindcore","guitar","hip-hop",\
                "honky-tonk","indie","jazz","k-pop","latin","new-age","opera","punk",\
                "show-tunes","singer-songwriter"]

track_count = 1000

for genre in seed_genres:
    track_url = 'https://api.spotify.com/v1/recommendations?' + 'seed_genres=' + genre + "&limit=100"

    data_path = "C:/Users/athor/Documents/git/SpotifyClassifier/Tracklists/"
    data_file = genre + ".json"
    data_fullpath = data_path + data_file

    # Construct Spotify API query
    headers = {
        'Authorization': 'Bearer '+ token,
        'Content-type': 'application/json',
    }

    count = 0
    nothing_new = 0
    tracks = {}
    #Break if reached desired number tracks OR no unique tracks seen in X iterations
    while count < track_count and nothing_new<20:
        # Query Spotify API
        try:
            response = requests.get(track_url, headers=headers).json()
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

        #print(count)
        

    with open(data_fullpath, 'w') as f:
        json.dump(tracks, f, indent=4)

    print("Completed Genre: " + genre + ", count: "+str(count))

