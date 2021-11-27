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

2. Run the Flask Appp:

```
$ flask run
```

Point your browser to http://localhost:5000/ to start making your collage!

Here is what to expect:

https://user-images.githubusercontent.com/238128/143720656-9dfdbe1f-8119-4dfb-9adc-9a321e69aa7b.mp4

Some things to consider:

- If multiple tracks from the same album appear in a playlist, the album's cover will be used only once in the collage.

- The preview uses 100px version of the album art but the download button generates the collage again using the higher resolution 300px version.

- While large playlists (100+ tracks) are supported, I've noticed that Safari (v15.1 running on macOS Monterey) really struggles with generating the 300px version. The Download button just fails and you get an invalid 3 KB PNG file. Chrome and Firefox don't have the same problem.

    - That said, the largest playlist I tried this with had 825 tracks across 757 albums and even Chrome and Firefox struggled a little there. The download button worked in Chrome but not in Firefox which simply downloaded a  0 KB PNG file.

    - Playlists with 100 tracks or so seems to be the sweet spot here.

    - My tests were run on a Mid-2015 Macbook Pro with 16 GB RAM, quad core i7 Intel processor running at 2.2 GHz and integrated Intel Iris Pro processor with 1536 MB memory. You might get better or worse results depending on your hardware.

- Chrome and Firefox also allow you to right-click the collage and save it as an image.
