from flask import Flask, Response, request
from flask.json.tag import JSONTag
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.wrappers import response

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Spotify-Local"
mongo = PyMongo(app)

@app.route("/playlists", methods=["GET"])
def get_playlists():
    response = mongo.db.Playlists.find().limit(10)
    playlists = json_util.dumps(response)
    return Response(playlists, mimetype="application/json")

@app.route("/playlists/<playlist_id>", methods=["GET"])
def get_playlist(playlist_id):
    response = mongo.db.Playlists.find_one({"_id": ObjectId(playlist_id)})
    playlist = json_util.dumps(response)
    return Response(playlist, mimetype="application/json")

@app.route("/playlists/<playlist_id>", methods=["PUT"])
def update_playlist(playlist_id):
    name = request.json["name"]
    mongo.db.Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$set": {"name": name}})
    return Response("", status=204)

@app.route("/playlists/<playlist_id>", methods=["DELETE"])
def delete_playlist(playlist_id):
    mongo.db.Playlists.delete_one({"_id": ObjectId(playlist_id)})
    return Response("", status=204)

@app.route("/playlists/<playlist_id>/tracks", methods=["POST"])
def add_track_to_playlist(playlist_id):
    
    track = {"artist_name": request.json["artist_name"], "track_name": request.json["track_name"], "album_name": request.json["album_name"]}
    response = mongo.db.Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$push": {"tracks": track}, "$inc": { "num_tracks": 1 } })
    #print(response)
    return Response(response, mimetype="application/json")


@app.route("/playlists/<playlist_id>/tracks/<track_name>", methods=["DELETE"])
def delete_track_from_playlist(playlist_id, track_name):
    response = mongo.db.Playlists.update_one({"_id": ObjectId(playlist_id)}, {"$pull": {"tracks": {"track_name" : track_name} }, "$inc": { "num_tracks": -1 }})
    return Response("", status=204)
if __name__ == '__main__':
    app.run(debug=True)