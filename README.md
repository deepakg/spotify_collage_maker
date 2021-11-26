# Spotify Collage Maker

This Flask application lets you make a collage of album covers in a Spotify playlist. You'll need to sign up with Spotify for a Client Id and a Client Secret.

Clone the repository, go into the spotify_collage_maker folder and run:

```
$ export FLASK_APP=spotify
$ flask run
```

Then point your browser to http://localhost:5000/

I'll update this file with detailed setup instructions, but in the meanwhile, here is how it looks:

https://user-images.githubusercontent.com/238128/143617592-6325cda6-a9d2-4c7b-ae36-fea6e0b93513.mov

Some things to consider:

- If multiple tracks from the same album appear in the playlist, it'll only use it once in the collage.

- The preview uses 100px versions of the album art but the download button would generate the collage again using the higher-res 300px versions.

- While large playlists (100+ tracks) are supported, I've noticed that Safari (v15.1 running on macOS Monterey) really struggles with the 300px version. The Download button just fails and you get an invalid 3 KB PNG file. Chrome and Firefox don't have the same problem. 

    - That said, the largest playlist I tried this with had 825 tracks across 757 unique albums and even Chrome and Firefox struggled a little there. The download button worked in Chrome but not in Firefox which simply downloaded a  0 KB PNG file.

    - Playlists with 100 tracks or so seems to be the sweet spot here.

    - My tests were run on a Mid-2015 Macbook Pro with 16 GB RAM, quad core i7 Intel processor running at 2.2 GHz and integrated Intel Iris Pro processor with 1536 MB memory. You might get better or worse results depending on your hardware.

- Chrome and Firefox also allow you to right-click the collage and save it as an image.
