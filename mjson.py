import json

def extract_song_info(json_content):
    # Load JSON content into a Python object
    data = json.loads(json_content)

    # Extract song information
    songs = data["songs"]
    song_dict = {}

    # Iterate over each song and extract title and artist
    for song in songs:
        title = song["title"]
        artist = song["artist"]
        song_dict[title] = artist

    return song_dict

# Example input string containing JSON
input_string = '''
Here's an example of an array of three KPOP songs in a JSON object:

{
  "songs": [
    {
      "title": "Song1",
      "artist": "Artist1"
    },
    {
      "title": "Song2",
      "artist": "Artist2"
    },
    {
      "title": "Song3",
      "artist": "Artist3"
    }
  ]
}
'''

# Find the JSON content within the input string
json_start = input_string.find("{")
json_end = input_string.rfind("}") + 1
json_content = input_string[json_start:json_end]

# Extract song information from JSON content
song_dict = extract_song_info(json_content)