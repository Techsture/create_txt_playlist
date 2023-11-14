#!/usr/bin/env python3

from wcwidth import wcswidth

# Reading the file content
file_path = '/Users/michaelandrews/Desktop/playlist.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Splitting each line into artist and track
data = []
for line in lines:
    parts = line.strip().split(' - ')
    if len(parts) == 2:
        data.append(parts)

# Determining the display width of each column
max_artist_length = max(wcswidth(artist) for artist, _ in data)
max_track_length = max(wcswidth(track) for _, track in data)

# Setting up the header
header_format = "{:<15} | {:<" + str(max_artist_length) + "} | {:<" + str(max_track_length) + "} | {}"
header = header_format.format("Track Number", "Artist", "Track", "Notes")
print(header)
print('-' * len(header))

# Printing each row
row_format = "{:<15} | {:<" + str(max_artist_length) + "} | {:<" + str(max_track_length) + "} | "
for i, (artist, track) in enumerate(data, start=1):
    print(row_format.format(i, artist, track))
