#!/usr/bin/python

import sys
import json

try:
  json_txt = sys.stdin.read().strip()
  playlists = json.loads(json_txt)
  songs = {}
  for playlist in playlists:
    tracks = playlist["tracks"]
    for track in tracks:
      count = songs.get(track["track_uri"],
        {
          "artist_name": track["artist_name"], 
          "track_name": track["track_name"], 
          "count": 0
        })
      count["count"] += 1
      songs[track["track_uri"]] = count
  for song, value in songs.items():
    print ("%s\t%s\t%s\t%d" % (song, value["artist_name"], value["track_name"], value["count"]))
except Exception as e:
  sys.stderr.write("Error: %s\n" % e)