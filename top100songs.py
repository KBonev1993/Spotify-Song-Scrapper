import requests
import os

# Define the URL and headers
url = 'https://spotifycharts.com/regional/global/daily/latest/download'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Make a request to download the CSV file
response = requests.get(url, headers=headers)

# Write the contents of the CSV file to a local file
with open('spotify_top_100.csv', 'wb') as f:
    f.write(response.content)

# Read the CSV file and extract the song names and artist names
with open('spotify_top_100.csv', 'r') as f:
    lines = f.readlines()
    songs = [line.split(',')[1] for line in lines[1:101]]
    artists = [line.split(',')[2] for line in lines[1:101]]

# Loop through each song and download it in WAV format
for i, song in enumerate(songs):
    artist = artists[i]
    query = f'{song} {artist}'
    response = requests.get(f'https://api.napster.com/v2.2/search/verbose?query={query}&type=track', headers=headers)
    track_id = response.json()['search']['data']['tracks'][0]['id']
    response = requests.get(f'https://api.napster.com/v2.2/tracks/{track_id}', headers=headers)
    audio_url = response.json()['tracks'][0]['previewURL']
    response = requests.get(audio_url, headers=headers)
    with open(f'{song}.wav', 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {song}.wav')

# Remove the CSV file
os.remove('spotify_top_100.csv')
