import requests
import pymongo
import time
from keys import keys

API_KEY = keys['lastfm_key']

connection = pymongo.Connection()
db = connection['worstbandever']
collection = db['artists']

def get_info(artist):
    payload = {'method':'artist.getinfo', 'artist':artist, 'api_key':API_KEY, 'format':'json'} 
    r = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
 
    listeners = (r.json['artist']['stats']['listeners'])
    playcount = (r.json['artist']['stats']['playcount'])
   
    return listeners, playcount

def update_database(artist, listeners, playcount):
    posts.update({'name': artist}, {'$set': {'listeners': listeners}})
    posts.update({'name': artist}, {'$set': {'playcount': playcount}})

posts = db.artists
artists = []

for post in posts.find():
    artists.append(post['name'])

for artist in artists:
    listeners, playcount = get_info(artist)
    update_database(artist, listeners, playcount)
    time.sleep(5)
