from flask import Flask
from spotipy.oauth2 import SpotifyClientCredentials
import tweepy, wikipedia, spotipy, jsonify,json

app = Flask(__name__)

auth = tweepy.OAuthHandler("hYbdgTfNZylDarmqS7FcsgeFq", "HANGiGZZiGmie0wD2MXhkbZrSITejToiLUulZt2iAWsKY2Lu6L")
#Uses OAuthHandler, consumer token and consumer secret
auth.access_token = "786725499024343041-IcJWwHcBzaG31rDCXHlHYOG4MTXS1k7"
auth.access_token_secret = "Qu5rE29KWvCM8Xp4DFFMfwd5MQJ9FqkYw2AEpA7yEXMcJ"
#Uses my access tokens, no idea if this is right, probably not safe but w/e
API = tweepy.API(auth) #Creates an instance of API

CLIENTID = '750b513588564b54abaef7745181a88e'
CLIENTSECRET = 'a8fac678b7664e368842c5864cf2e927'
clientCreds = SpotifyClientCredentials(client_id= CLIENTID, client_secret= CLIENTSECRET)
sp = spotipy.Spotify(client_credentials_manager=clientCreds)

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

@app.route('/rec/<queryG>')
def generalQuery(queryG):
    if len(sp.search(q=queryG,type='artist')['artists']['items']) == 0:
        return jsonify.dumps(sp.search(q=queryG, type='track'))
    wikiSug = wikipedia.suggest(query=queryG)
    artistID = json.dumps(sp.search(q=queryG,type='artist')['artists']['items'][0]['uri'])#artist_top_tracks(artist_id, country='US')
    id = artistID[16:len(artistID)-1]
    spotRecs = sp.recommendations(seed_artists=[id], limit=10)
    return json.dumps(spotRecs)

if __name__ == '__main__':
    app.run()