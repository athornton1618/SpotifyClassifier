# SpotifyClassifier
EECS E6893 Research Project - Columbia University Fall 2021

## Abstract
Songs in mp3 file format will be processed into beat per minute histogram / short time fourier transform as a vectorized embedded format. 1000+ mp3 files will be sourced, vectorized, and classified using a k-genre clustering algorithm. Eventually, the model should be able to take in a new song, process it into vector form, and classify based on nearest cluster. We will be using the Spotify developer API to collect song metadata and snippets for signal pre-processing, and Google Cloud platform for data storage and model computations.

## Architecture
![Alt text](https://github.com/athornton1618/SpotifyClassifier/blob/main/Documentation/SystemArchitecture.png?raw=true) 

## Contributors
* Alex Thornton     (apt2141)	
* Elmira Aliyeva    (ea2970)
* Tanvi Pande       (tp2673)

## References
This will be a big data expansion on this concept from Princeton: https://soundlab.cs.princeton.edu/publications/2001_ismir_amgc.pdf
