# BBC Thumbnails
A python program for downloading thumbnails for BBC television series. It uses the episode or series PID to download matching thumbnails.
## Getting Started
###### Prerequisites
The only prerequisite for now is BeautifulSoup. It can be downloaded from this website: [Crummy BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
###### First run
The first run of the program must be done with **--config**, for instance:
```
python bbcthumb.py --config
Input the wanted default resolution: 1920x1080
Input the wanted default destination: C:/Users/User/Desktop
Do you want to skip episode name fetching (1 for yes, 0 for no): 0
Saved config! Closing.
```
## Using the program
###### One episode thumbnail
To download the thumbnail of one episode of a series (in other words one pid of an episode), do the following:
```
python bbcthumb.py [pid]
```
where **[pid]** is replaced with the pid of the wanted episode. The program will find the thumbnail link, adjust the resolution and download it to the default download directory.
###### Multiple episode thumbnails
Downloading thumbnails for multiple episodes is the same as it is for one, just add more pids. For instance:
```
python bbcthumb.py [pid] [pid] [pid] 
```
The program will seek links for all of them and download them one after the other. The same error might be seen as in the first example.
###### Downloading series thumbnails
When downloading thumbnails for an entire series of a programme use the series pid rather than a single episode pid and use the argument --series, like this:
```
python bbcthumb.py --series [pid]
```
The program creates an additional folder in the download directory that has the series name so that all thumbnails of a single series are in one place.

This is it for now, more info and perhaps a wiki page with upcoming updates.
