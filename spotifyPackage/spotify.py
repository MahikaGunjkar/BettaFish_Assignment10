# spotify.py
# Name: Ben Ujvagi, Mahika Gunjkar
# email: ujvagibw@mail.uc.edu, gunjkamg@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Use an API to change a JSON to a .csv

# Brief Description of what this module does. This module finds the spotify API and links the account to the project
# Citations:
# Anything else that's relevant:

import requests
import base64
import csv

class SpotifyHandler:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = "https://accounts.spotify.com/api/token"
        self.base_url = "https://api.spotify.com/v1/"
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Fetches a new access token from Spotify API."""
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode()).decode()

        response = requests.post(self.token_url, headers={
            "Authorization": f"Basic {client_creds_b64}"
        }, data={
            "grant_type": "client_credentials"
        })

        if response.status_code == 200:
            print("Access token obtained successfully.")
            return response.json().get('access_token')
        else:
            print(f"Error obtaining access token: {response.status_code}")
            raise Exception("Failed to get access token from Spotify")

    def fetch_new_releases(self, limit=10):
        """Fetches the latest new releases from Spotify."""
        endpoint = f"{self.base_url}browse/new-releases?limit={limit}"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            data = response.json()
            albums_info = []

            for album in data['albums']['items']:
                album_info = {
                    "album_name": album["name"],
                    "artist_name": album["artists"][0]["name"],
                    "release_date": album["release_date"],
                    "total_tracks": album["total_tracks"],
                    "album_type": album["album_type"],
                    "spotify_url": album["external_urls"]["spotify"]
                }
                albums_info.append(album_info)
            return albums_info
        else:
            print(f"Error fetching new releases: {response.status_code}")
            raise Exception("Failed to fetch new releases from Spotify")

    def save_to_csv(self, data, filename='spotify_new_releases.csv'):
        """Writes the list of album data to a CSV file."""
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error in save_to_csv: {e}")
