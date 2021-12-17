# SpotifyClassifier
EECS E6893 Research Project - Columbia University Fall 2021

<img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/logo.png width="200">

## Contributors
* Alex Thornton     (apt2141)	
* Elmira Aliyeva    (ea2970)
* Tanvi Pande       (tp2673)

## Use Case

Users are curious about 'Spotify Wrapped' genre listening patterns
Spotify API only provides genre labels for artists, not tracks
Some artists have many genres

## Abstract
Music genre classification is a complex task, which can even be difficult for humans. Using a Spotify Developer account to interface with their API, we have created our own dataset and a music genre classifier capable of identifying song genres across a much larger range of genres and subgenres than previously achieved in academic research. Additionally, we leverage Spotify's pre-processed track metadata, allowing for genre classification with only a song name as an input, rather than an audio mp3 file.

## Dataset
* Queried Spotify for recommendations across 73 subgenres
* ~500 tracks labelled for each subgenre
* Collected Spotify metadata for individual tracks, added subgenre labels
* Grouped 73 subgenres ->11 'super-genres' for simpler classification

<img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/GenreHierarchy.PNG width="400">

## Architecture
<img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/SystemArchitecture.png> 

## Analysis
* Maybe 'super-genre' hierarchy model was an oversimplification

* Perhaps some subgenres belong to more than one cluster

* Ex: "alt-rock" = "rock"&"alternative"

* We set out to find more representative super-genres

* Also want to identify problematic (highly interconnected) subgenres

* Ranked based on subgenre overlap 

* 'chill', 'study', and 'sleep', rounded out the top 3

* Interestingly, these were all part of our 'easy-listening' super-genre 

* 'guitar', 'party, and 'acoustic' are unsurprising offenders, as they are vague



