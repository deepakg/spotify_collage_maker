# Spotify Collage Maker

This Flask application lets you make a collage of album covers in a Spotify playlist. You'll need to sign up with Spotify for a Client Id and a Client Secret.

Here are a couple of ways you can run this on your machine:

Clone/download this repository to your machine and change your directory to it.

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).

2. Build the Docker container image:

```
$ docker build --tag spotify_collage_maker .
```

3. Run the Docker container image:

```
$ docker run --publish 5000:5000 spotify_collage_maker
```

Don't want to install Docker and have Python 3.8 or higher on your machine already?

1. Install the dependencies on your machine:

```
$ pip3 install -r requirements.txt
```

2. Run the Flask App:

```
$ flask run
```

Point your browser to http://localhost:5000/ to start making your collage!

Here is what to expect:

https://user-images.githubusercontent.com/238128/144763084-724e0f99-01d6-4e80-b69d-c3cd55a8c891.mp4

Some things to consider:

- If multiple tracks from the same album appear in a playlist, the album's cover will be used only once in the collage.

- The preview uses 100px version of the album art but the download button generates the collage again using the higher resolution 300px version.

- While large playlists (100+ tracks) are supported, the performance will vary based on your machine's configuration and the browser you are using. The Download button might not work with very large playlists (500+) on browsers other than Chrome.

- Chrome and Firefox also allow you to right-click the collage and save it as an image. You will get the low-resolution 100px version in that case though.
