from flask import Flask, render_template, request, make_response
from spotify_downloader import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    spotify_client_id = ""
    spotify_client_secret = ""
    spotify_playlist_url = ""
    playlist_items = []
    img_urls = []
    if request.method == "POST":
        spotify_client_id = request.form.get("spotify_client_id", "")
        spotify_client_secret = request.form.get("spotify_client_secret")
        spotify_playlist_url = request.form.get("spotify_playlist_url", "")
        if spotify_client_id and spotify_client_secret and spotify_playlist_url:
            playlist_id = get_playlist_id(spotify_playlist_url)
            spotify_client = get_spotify_client(spotify_client_id, spotify_client_secret)
            playlist_items = get_playlist_items(spotify_client, playlist_id)
            img_urls = get_image_urls(playlist_items, width=300)

    return render_template('index.html',
                           spotify_client_id=spotify_client_id,
                           spotify_client_secret=spotify_client_secret,
                           spotify_playlist_url=spotify_playlist_url,
                           items=playlist_items,
                           img_urls=img_urls)
