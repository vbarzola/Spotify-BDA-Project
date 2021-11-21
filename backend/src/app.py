from flask import Flask, Response, request
from flask.json.tag import JSONTag
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.wrappers import response

import subprocess

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://34.70.139.149:27017/test"
mongo = PyMongo(app)
collection = mongo.db.SpotifyDatabase
@app.route("/playlists", methods=["GET"])
def get_playlists():
    response = collection.find().limit(10)
    playlists = json_util.dumps(response)
    return Response(playlists, mimetype="application/json")

@app.route("/mapReduce", methods=["GET"])
def get_mapReduce():
    bashCommand = "hdfs dfs -cat gs://datos-spotify/output/prueba8/part* | sort -t$'\\\\\\\t' -k 3 -n -r"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    req = output.splitlines()[0]
    return Response(req, mimetype="application/json")

@app.route("/playlists/<playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    response = collection.find_one({"_id": ObjectId(playlist_id)})
    playlist = json_util.dumps(response)
    return Response(playlist, mimetype="application/json")

@app.route("/playlists/<playlist_id>", methods=["PUT"])
def update_playlist(playlist_id):
    name = request.json["name"]
    collection.update_one({"_id": ObjectId(playlist_id)}, {"$set": {"name": name}})
    return Response("", status=204)

@app.route("/playlists/<playlist_id>", methods=["DELETE"])
def delete_playlist(playlist_id):
    collection.delete_one({"_id": ObjectId(playlist_id)})
    return Response("", status=204)

@app.route("/playlists/<playlist_id>/tracks", methods=["POST"])
def add_track_to_playlist(playlist_id):
    
    track = {"artist_name": request.json["artist_name"], "track_name": request.json["track_name"], "album_name": request.json["album_name"]}
    response = collection.update_one({"_id": ObjectId(playlist_id)}, {"$push": {"tracks": track}, "$inc": { "num_tracks": 1 } })
    #print(response)
    return Response(response, mimetype="application/json")


@app.route("/playlists/<playlist_id>/tracks/<track_name>", methods=["DELETE"])
def delete_track_from_playlist(playlist_id, track_name):
    response = collection.update_one({"_id": ObjectId(playlist_id)}, {"$pull": {"tracks": {"track_name" : track_name} }, "$inc": { "num_tracks": -1 }})
    return Response("", status=204)
if __name__ == '__main__':
    app.run(debug=True)