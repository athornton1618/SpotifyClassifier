# SpotifyClassifier
EECS E6893 Research Project - Columbia University Fall 2021

<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/logo.png width="300">
<p/>

## Contributors
1. Alex Thornton     (apt2141)	
2. Elmira Aliyeva    (ea2970)
3. Tanvi Pande       (tp2673)

## Abstract
Music genre classification is a complex task, which can even be difficult for humans. Using a Spotify Developer account to interface with their API, we have created our own dataset and a music genre classifier capable of identifying song genres across a much larger range of genres and subgenres than previously achieved in academic research. Additionally, we leverage Spotify's pre-processed track metadata, allowing for genre classification with only a song name as an input, rather than an audio mp3 file.

## Use Case

* Users are curious about 'Spotify Wrapped' genre listening patterns
* Spotify API only provides genre labels for artists, not tracks
* Some artists have many genres

<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/TSwiftie.png >
<p/>

## Dataset
* Queried Spotify for recommendations across 73 subgenres
* ~500 tracks labelled for each subgenre
* Collected Spotify metadata for individual tracks, added subgenre labels
* Grouped 73 subgenres ->11 'super-genres' for simpler classification

<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/GenreHierarchy.PNG width="400">
<p/>

## Model Architecture
<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/SystemArchitecture.png width="650"> 
<p/>

## Performance

<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/confusion.PNG width="400">
<p/>

### Tested models
* Random Forest Classifier. Accuracy: 0.4765
* Decision Tree Classifier. Accuracy: 0.4156
* Logistic Regression. Accuracy: 0.5518
* LinearSVC. Accuracy: 0.4796
* GBT Classifier Accuracy: 0.6223
### GBT results
* Test set F1-Score: 0.6217
* Test set Precision: 0.6238
* Test set Recall:  0.6223
* Test set Accuracy: 0.6223
### Comparison to Human Performance
As a benchmark, human accuracy averages around 70% for this kind of genre classification work [1].


## Analysis
* Maybe 'super-genre' hierarchy model was an oversimplification

* Perhaps some subgenres belong to more than one cluster

* Ex: "alt-rock" = "rock"&"alternative"

* We set out to find more representative super-genres

* Also want to identify problematic (highly interconnected) subgenres

<img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/Analysis.PNG >

* Ranked based on subgenre overlap 

* 'chill', 'study', and 'sleep', rounded out the top 3

* Interestingly, these were all part of our 'easy-listening' super-genre 

* 'guitar', 'party, and 'acoustic' are unsurprising offenders, as they are vague

<p align="center">
  <img src=https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/TopOffenders.png >
<p/>

## References
1. Mingwen Dong. Convolutional neural network achieves human-level accuracy in music genre classification. CoRR, abs/1802.09697, 2018.

## Thank You
Copyright (c) 2021 Alex Thornton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


