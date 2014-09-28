import flask
import pymongo
import tweet
from random import choice
from bson.objectid import ObjectId
from os import urandom
from keys import keys

connection = pymongo.Connection()
db = connection['worstbandever']
collection = db['artists']

posts = db.artists

artists = []

for post in posts.find():
    artists.append(post)

def get_artists():
    artist1 = choice(artists)
    artist2 = choice(artists)
    while artist2 == artist1:
        artist2 = choice(artists)

    return (artist1, artist2)

def update_stats(artist_id):
    artist = posts.find_one({'_id':artist_id})

    return (artist['playcount'], artist['listeners'])   

def check_top():
    for post in posts.find().sort('votes', -1).limit(1):
        top = post    

    return top

def send_tweet(artist):
    tweet.send_tweet(artist[:116] + ' is now the worst band!') 

app = flask.Flask(__name__)
app.secret_key = keys['flask']

@app.route('/', methods=['GET','POST'])
def main():
    if flask.request.method == 'POST':
        if 'session_id' in flask.session:
            artist = flask.request.form['button']
            full_id = ObjectId(artist)
            posts.update({'_id': full_id}, {'$inc':{'votes': 1}})
            if check_top == artist:
                send_tweet(artist['name'])

        return flask.redirect('/', code=303)

    artist1, artist2 = get_artists()
    playcount1, listeners1 = update_stats(artist1['_id'])
    playcount2, listeners2 = update_stats(artist2['_id'])

    if 'session_id' not in flask.session:
        flask.session['session_id'] = urandom(24)

    return flask.render_template('main.html', artist1=artist1, artist2=artist2, playcount1=playcount1, playcount2=playcount2, listeners1=listeners1, listeners2=listeners2)

@app.route('/top')
def top():
    top = []
    for post in posts.find().sort('votes', -1).limit(10):
        top.append(post)

    return flask.render_template('top.html', top=top)

if __name__ == '__main__':
    app.run()
