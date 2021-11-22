from flask import Flask, Response, request
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
from decouple import config

import subprocess

app = Flask(__name__)
MONGO_HOST = config('MONGO_HOST', 'localhost')
MONGO_PORT = config('MONGO_PORT', 27017)
MONGO_DBNAME = config('MONGO_DBNAME', 'test')
MONGO_USERNAME = config('MONGO_USERNAME', 'test')
MONGO_PASSWORD = config('MONGO_PASSWORD', 'test')
MONGO_AUTH_SOURCE = config('MONGO_AUTH_SOURCE', 'admin')

app.config['MONGO_URI'] = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DBNAME}?authSource={MONGO_AUTH_SOURCE}'

mongo = PyMongo(app)

CORS(app)

Playlists = mongo.db.Playlists

@app.route("/playlists", methods=["GET"])
def get_playlists():
    response = Playlists.find().limit(10)
    playlists = json_util.dumps(response)
    return Response(playlists, mimetype="application/json")

@app.route("/playlists/<playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    try:
      response = Playlists.find_one({"_id": ObjectId(playlist_id)})
      playlist = json_util.dumps(response)
      return Response(playlist, mimetype="application/json")
    except:
      return Response(status=404)

@app.route("/playlists/<playlist_id>", methods=["PUT"])
def update_playlist(playlist_id):
    try:
      name = request.json["name"]
      Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$set": {"name": name}})
      return Response("", status=204)
    except:
      return Response(status=404)

@app.route("/playlists/<playlist_id>", methods=["DELETE"])
def delete_playlist(playlist_id):
    Playlists.delete_one({"_id": ObjectId(playlist_id)})
    return Response("", status=204)

@app.route("/playlists/<playlist_id>/tracks", methods=["POST"])
def add_track_to_playlist(playlist_id):
    try:
      track = {"artist_name": request.json["artist_name"], "track_name": request.json["track_name"], "album_name": request.json["album_name"]}
      response = Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$push": {"tracks": track}, "$inc": { "num_tracks": 1 } })
      return Response(response, mimetype="application/json")
    except:
      return Response(status=404)


@app.route("/playlists/<playlist_id>/tracks/<track_name>", methods=["DELETE"])
def delete_track_from_playlist(playlist_id, track_name):
    try:
      Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$pull": {"tracks": {"track_name" : track_name} }, "$inc": { "num_tracks": -1 }})
      return Response("", status=204)
    except:
      return Response(status=404)

@app.route("/mapReduce", methods=["GET"])
def get_map_reduce():
    bashCommand = "hdfs dfs -cat gs://datos-spotify/output/spotifyPlaylists/part*"
    try:
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    except:
        return Response(json_util.dumps({"status": "error"}), mimetype="application/json")
    output, error = process.communicate()
    results = output.splitlines()
    max_frecuent_song = {"artist": "", "song": "", "frecuency": 0}
    for result in results:
        result = result.split("\t")
        if int(result[2]) > max_frecuent_song["frecuency"]:
            max_frecuent_song["artist"] = result[0]
            max_frecuent_song["song"] = result[1]
            max_frecuent_song["frecuency"] = int(result[2])
    return Response(json_util.dumps(max_frecuent_song), mimetype="application/json")

@app.route("/doMapReduce", methods=["GET"])
def get_do_map_reduce():
    try:
        remove_command = "hdfs dfs -rm -r gs://datos-spotify/output/spotifyPlaylistsTmp"
        process = subprocess.Popen(remove_command.split(), stdout=subprocess.PIPE)
        process.communicate()
    except:
        pass
    try:
        process = subprocess.Popen([
            'hadoop',
            'jar',
            '/usr/lib/hadoop/hadoop-streaming.jar',
            '-files',
            'gs://datos-spotify/mapper.py,gs://datos-spotify/reducer.py',
            '-mapper',
            'python ./mapper.py',
            '-reducer',
            'python ./reducer.py',
            '-input',
            'gs://datos-spotify/Data/*',
            '-output',
            'gs://datos-spotify/output/spotifyPlaylistsTmp'
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()
        copy = "hdfs dfs -cp -f gs://datos-spotify/output/spotifyPlaylistsTmp/* gs://datos-spotify/output/spotifyPlaylists"
        process = subprocess.Popen(copy.split(), stdout=subprocess.PIPE)
        process.communicate()
        return Response(json_util.dumps({"status": "ok"}), mimetype="application/json")
    except:
        return Response(json_util.dumps({"status": "error"}), mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True)