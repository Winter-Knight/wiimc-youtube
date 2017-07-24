# Background
On July 28, 2017, Youtube stopped supporting their Wii Youtube channel. In
response, there was a request to make WiiMC able to download and play Youtube
videos. The file youtube.py, properly set up with a web server, and
onlinemedia.xml, set up with WiiMC, allows WiiMC to view Youtube videos.

# Setup
## Prerequisites

- A modded Wii, enabled to run Homebrew applications.
- WiiMC
- A web server that can run Python2 cgi scripts.
- youtube-dl on your web server


## How to setup youtube.py

1. Copy youtube.py to your web server's cgi directory.

2. Edit the media_dir line of youtube.py. Point media_dir to whatever directory
you want your cache of youtube files to be in.

3. Install the youtube-dl binary (https://rg3.github.io/youtube-dl/download.html)
into your path (such as /usr/local/bin/)

4. Edit WiiMC's onlinemedia.xml file. This is a settings file, probably on your
SD card, probably in the apps/wiimc/ directory. The Youtube lines, by default,
look like this:

```html
<link name="YouTube" addr="http://www.wiimc.org/media/youtube.php" />
<link name="YouTube - Search" type="search" addr="http://www.wiimc.org/media/youtube.php?q=" />
```
Edit them to look more like this:
```html
<link name="YouTube" type="search" addr="http://yourdomainorip/yourpathtoyoutubepy/youtube.py?watch=" />
<link name="YouTube - Search" type="search" addr="http://yourdomainorip/yourpathtoyoutubepy/youtube.py?query=" />
```
Note that they are now both type="search" and they both point to youtube.py.

# Warning regarding bandwidth.

All video files must go through your web server. This is a requirement because 
WiiMC only supports http connections, and Youtube only supports https
connections. This project enables a web server to act as a bridge between WiiMC
and Youtube. If your web server is remote, your web server will be using
bandwidth to pull the video from Youtube, and also to push the video to your
Wii.
