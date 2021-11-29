import json

tracklist_dir = "C:/Users/athor/Documents/git/SpotifyClassifier/Tracklists/"

genres = ["ambient","alternative","anime","blues","classical","country","death-metal","dubstep",\
            "electronic","folk","gospel","goth","grindcore","guitar","hip-hop",\
            "honky-tonk","indie","jazz","k-pop","latin","new-age","opera","punk",\
            "show-tunes","singer-songwriter"]

print("---Tracklist Summary---")
for genre in genres:
    file = tracklist_dir + genre + ".json"
    with open(file, "r") as tracklist:
        tracklist = json.load(tracklist)
        num_songs = len(tracklist.keys())
    print("Genre: "+genre+", # Tracks: "+str(num_songs))