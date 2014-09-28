import requests
import pymongo
from keys import keys

API_KEY = keys['lastfm_key']
API_SECRET = keys['lastfm_secret']

payload = {'method':'chart.gettopartists', 'limit':'1000', 'api_key':API_KEY, 'format':'json'} 
r = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)

artists = []

for item in (r.json()['artists']['artist']):
    del item['streamable']
    del item['mbid']
    item['votes'] = 0
    for picture in item['image'][:]:
        if picture['size'] == 'extralarge':
            item['pic'] = picture['#text']
    del item['image']
    artists.append(item)

connection = pymongo.Connection()
db = connection['worstbandever']
collection = db['artists']

posts = db.artists

posts.insert(artists)
