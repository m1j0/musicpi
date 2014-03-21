#MisicPi

This is an Project I work on my spare time. It is aimed to be a music player for parties, where your friends can contribute and vote for music they'd like to listen to.

The user interface is intended to be a web interface and later there should be an Android-app provided. 

##The plan so far
- [ ] Write the web interface with an [django](https://www.djangoproject.com/) framework powered back-end.
	- Actually I've got stuck on Implementing an m2m relationship in genre with an intermediate table which represents an weighted edge. 
- [ ] Connecting the [mpd](http://www.musicpd.org/) as audio player to the front-end.
- [ ] Extracting an XML interface to provide a point, where the Android app could be bind to.
- [ ] Writing the Android app.