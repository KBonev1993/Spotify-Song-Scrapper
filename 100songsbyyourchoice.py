import requests
import os

# Define the URL and headers
url = 'https://api.napster.com/v2.2/search/verbose'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'apikey': 'API_KEY'
}

# Get input from the user
songs = []
for i in range(100):
    song = input(f'Enter the name of song {i+1}: ')
    songs.append(song)

# Loop through each song and download it in WAV format
for i, song in enumerate(songs):
    query = f'{song}'
    response = requests.get(f'{url}?query={query}&type=track', headers=headers)
    track_id = response.json()['search']['data']['tracks'][0]['id']
    response = requests.get(f'https://api.napster.com/v2.2/tracks/{track_id}', headers=headers)
    audio_url = response.json()['tracks'][0]['previewURL']
    response = requests.get(audio_url, headers=headers)
    with open(f'{song}.wav', 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {song}.wav')

