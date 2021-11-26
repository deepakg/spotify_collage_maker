import os

from pathlib import PurePath
from pprint import pprint
from urllib.parse import urlparse

import requests
import spotipy
import spotipy.oauth2 as oauth2


def get_spotify_client(client_id, client_secret):
    credentials = oauth2.SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret)

    token = credentials.get_access_token(as_dict=False)
    spotify = spotipy.Spotify(auth=token)

    return spotify

def get_playlist_items(spotify_client, playlist_id):
    if not spotify_client:
        return []
    playlist = spotify_client.user_playlist_tracks("", playlist_id)
    items = playlist['items']
    while playlist['next']:
        playlist = spotify_client.next(playlist)
        items.extend(playlist['items'])

    return items

def get_image_urls(playlist_items, width=640):
    urls = []
    for item in playlist_items:
        if item['track']['album']['images']:
            for image in item['track']['album']['images']:
                if image['width'] == width:
                    urls.append(image['url'])
                    break

    return urls

def get_playlist_id(playlist_url):
    parsed_url = urlparse(playlist_url)
    playlist_id = parsed_url.path.split("/")[-1]
    return playlist_id
