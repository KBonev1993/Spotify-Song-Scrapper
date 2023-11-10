Overview
This repository contains two Python scripts designed for automating the process of downloading music. The scripts interact with various APIs to fetch and download song previews in WAV format. They are useful for music enthusiasts who want to quickly download a collection of songs.

Script Descriptions
1. Spotify Top 100 Downloader (spotify_top_100_downloader.py)
This script automatically downloads the latest Top 100 songs from Spotify's global charts. It performs the following functions:

Fetches the current Top 100 songs from Spotify's global daily charts in CSV format.
Parses the CSV to extract song and artist names.
Uses the Napster API to find and download a preview of each song in WAV format.
Cleans up by removing the downloaded CSV file after processing.
2. Custom Song Downloader (custom_song_downloader.py)
This script allows users to download previews of songs of their choice in WAV format. It works as follows:

Prompts the user to input the names of up to 100 songs.
For each song, it searches the Napster API to find the track.
Downloads a preview of each track in WAV format.
Features
Automated Downloading: Both scripts automate the process of downloading song previews, saving time and effort.
API Integration: They leverage the Spotify and Napster APIs for fetching song data and previews.
User Interaction: The custom song downloader script interacts with the user to receive input for song names.
File Handling: The scripts handle file operations, including writing downloaded content to WAV files and managing temporary files.
How to Use
Run spotify_top_100_downloader.py to download the latest Spotify Top 100 songs.
Run custom_song_downloader.py and input the names of the songs you wish to download when prompted.
Dependencies
Python 3.x
requests for API calls
os for file and directory operations
Disclaimer
These scripts are intended for educational and personal use only. Ensure compliance with the terms of service of the respective APIs and respect copyright laws. The scripts download only previews of songs, not the full tracks.
