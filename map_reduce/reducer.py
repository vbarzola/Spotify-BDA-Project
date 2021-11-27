#!/usr/bin/python

import sys

songs = {}
try:
  for line in sys.stdin:
    song_uri, artist_name, song_name, count = line.strip().split("\t")
    song = songs.get(song_uri, 
      {
        "artist_name": artist_name, 
        "song_name": song_name, 
        "count": 0
      })
    song["count"] += int(count)
    songs[song_uri] = song

  max_song = {} # song with max count
  for song_uri, song in songs.items():
    if max_song == {} or max_song["count"] < song["count"]:
      max_song = song

  print ("%s\t%s\t%d" % (max_song["artist_name"], max_song["song_name"], max_song["count"]))
except:
  pass