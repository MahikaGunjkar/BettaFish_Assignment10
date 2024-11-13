# main.py
# spotify.py
# Name: Ben Ujvagi, Mahika Gunjkar
# email: ujvagibw@mail.uc.edu, gunjkamg@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Use an API to change a JSON to a .csv

# Brief Description of what this module does. This modules call the API through the client_id and client_secret. It also has the main entering code.
# Citations:
# Anything else that's relevant:

from spotifyPackage.spotify import SpotifyHandler

if __name__ == "__main__":
    def main():
        # Replace with your actual Spotify API credentials
        client_id = 'a17ac6d369964fae83ce1d181f76a852'
        client_secret = '2413589cff214479b4126ec79ba15cd8'

        try:
            # Initialize 
            handler = SpotifyHandler(client_id, client_secret)

            # Fetch 
            new_releases_data = handler.fetch_new_releases(limit=20)

            handler.save_to_csv(new_releases_data, filename="spotify_new_releases.csv")

        except Exception as e:
            print(f"Error in main: {e}")

    main()

