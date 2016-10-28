from flask import Flask
import tweepy, wikipedia, spotipy, jsonify,json

app = Flask(__name__)

auth = tweepy.OAuthHandler("hYbdgTfNZylDarmqS7FcsgeFq", "HANGiGZZiGmie0wD2MXhkbZrSITejToiLUulZt2iAWsKY2Lu6L")
#Uses OAuthHandler, consumer token and consumer secret
auth.access_token = "786725499024343041-IcJWwHcBzaG31rDCXHlHYOG4MTXS1k7"
auth.access_token_secret = "Qu5rE29KWvCM8Xp4DFFMfwd5MQJ9FqkYw2AEpA7yEXMcJ"
#Uses my access tokens, no idea if this is right, probably not safe but w/e
API = tweepy.API(auth) #Creates an instance of API

sp = spotipy.Spotify()

@app.route('/') #May as well have something here
def index():
    return 'Twitter API Proxy mini project'

@app.route('/twitter/<queryT>') #Based on keyword, works OK I guess
def keywordSearch(queryT):
    output = ""
    for val in API.search(q=queryT):
        output += val.text + "\n\n"
    return output

@app.route('/wiki/<queryW>')
def wikiTest(queryW):
    outputW = ""
    if len(wikipedia.search(queryW)) == 0:
        return "No article"
    outputW = wikipedia.summary(wikipedia.search(queryW)[0])
    return outputW

@app.route('/spotify/<queryS>') #Assume artist for now
def spotTest(queryS): #Search returns dict type
    #spotJson = json.loads(sp.search(q=queryS,type='artist'))
    if len(sp.search(q=queryS,type='artist')['artists']['items']) == 0:
        return jsonify.dumps(sp.search(q=queryS, type='track'))
    artistID = json.dumps(sp.search(q=queryS,type='artist')['artists']['items'][0]['uri'])#artist_top_tracks(artist_id, country='US')
    id = artistID[16:len(artistID)-1]
    return json.dumps(sp.artist_top_tracks(artist_id=id))

if __name__ == '__main__':
    app.run()