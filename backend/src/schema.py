from pymongo import MongoClient
from decouple import config
MONGO_HOST = config('MONGO_HOST', 'localhost')
MONGO_PORT = config('MONGO_PORT', 27017)
MONGO_DBNAME = config('MONGO_DBNAME', 'test')
MONGO_USERNAME = config('MONGO_USERNAME', 'test')
MONGO_PASSWORD = config('MONGO_PASSWORD', 'test')
MONGO_AUTH_SOURCE = config('MONGO_AUTH_SOURCE', 'admin')

MONGO_URI= 'mongodb://'+MONGO_USERNAME+':'+MONGO_PASSWORD+'@'+MONGO_HOST+':'+str(MONGO_PORT)+'/'+MONGO_DBNAME+"?authSource="+MONGO_AUTH_SOURCE
def create_playlist_collection():
    db = MongoClient(MONGO_URI).get_database()
    db.create_collection('Playlists2.0', validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'properties': {
                'name': {
                    'bsonType': 'string'
                },
                'collaborative': {
                    'bsonType': 'string'
                },
                'pid': {
                    'bsonType': 'number'
                },
                'modified_at':{
                    'bsonType': 'number'
                },
                'num_tracks':{
                    'bsonType': 'number'
                },
                'num_albums':{
                    'bsonType': 'number'
                },
                'num_followers':{
                    'bsonType': 'number'
                },
                'num_edits':{
                    'bsonType': 'number'
                },
                'duration_ms':{
                    'bsonType': 'number'
                },
                'num_artists':{
                    'bsonType': 'number'
                },
                'tracks':{
                    'bsonType': 'array',
                    'items': {
                        'bsonType': 'object',
                        'additionalProperties': True,
                        'properties': {
                            'pos': {
                                'bsonType': 'number'
                            },
                            'artist_name': {
                                'bsonType': 'string'
                            },
                            'artist_uri': {
                                'bsonType': 'string'
                            },
                            'track_uri': {
                                'bsonType': 'string'
                            },
                            'track_name': {
                                'bsonType': 'string'
                            },
                            'album_uri': {
                                'bsonType': 'string'
                            },
                            'album_name': {
                                'bsonType': 'string'
                            },
                            'duration_ms': {
                                'bsonType': 'number'
                            }
                        }
                    }
                }
            
            }
        }
    })
 
  
 

if __name__ == '__main__':
    create_playlist_collection()