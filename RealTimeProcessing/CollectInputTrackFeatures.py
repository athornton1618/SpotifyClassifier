import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
import numpy as np
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

os.environ['SPOTIPY_CLIENT_ID'] = 'SECRET'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'SECRET'

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
with open('C:/Users/athor/Documents/git/SpotifyClassifier/data/track_data.json') as json_file:
    data = json.load(json_file)

features = [[data['id'], data["super-genre-label"], data["subgenre-label"], data["danceability"], data['energy'],
                                      data['loudness'], data['mode'], data['speechiness'], data['acousticness'],
                                      data['instrumentalness'], data['liveness'], data['valence'],
                                      data['tempo'], data['time_signature'], data["popularity"], data["avg_pitches"],
                                      data["avg_timbre"]]]

dataframe = pd.DataFrame(features, columns=['id', 'super-genre', 'subgenre', 'danceability', 'energy',
                                          'loudness', 'mode', 'speechiness', 'acousticness',
                                          'instrumentalness', 'liveness', 'valence',
                                          'tempo', 'time_signature', 'popularity', 'avg_pitches', 'avg_timbre'])

split_df = pd.DataFrame(list(dataframe['avg_pitches']), columns=["pitch" + str(i) for i in range(12)])
dataframe = pd.concat([dataframe, split_df], axis=1)
dataframe = dataframe.drop('avg_pitches', axis=1)

split_df = pd.DataFrame(list(dataframe['avg_timbre']), columns=["timbre" + str(i) for i in range(12)])
dataframe = pd.concat([dataframe, split_df], axis=1)
dataframe = dataframe.drop('avg_timbre', axis=1)

spark = SparkSession.builder.master('local[*]').appName('data-processing').getOrCreate()
sparkDF = spark.createDataFrame(dataframe) 

### LOAD TRAINED MODEL
# load from local Model/model dir (the model is inside Model/model folder in project repo) 
pipelineModel = PipelineModel.load("../Model/model")

### CLASSIFY SONG
sparkDF = pipelineModel.transform(sparkDF)
sparkDF.select("prediction").show()
label_mapping = ['dance', 'pop', 'alternative', 'rock', 'hardcore', 'latin', 'country', 'jazz', 'classical', 'musical']
row_list = sparkDF.select("prediction").collect()
pred = [ int(row.prediction) for row in row_list]

### SEND OUTPUT BACK TO FRONT END
predicted_genre_str = label_mapping[pred[0]]
