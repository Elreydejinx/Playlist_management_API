
def linear_search(songs, song_id):
    for song in songs:
        if song.id == song_id:
            return song
    return None

def sort_songs(songs, key='name'):
    if key == 'name':
        return sorted(songs, key=lambda x: x.name)
    elif key == 'artist':
        return sorted(songs, key=lambda x: x.artist)
    elif key == 'genre':
        return sorted(songs, key=lambda x: x.genre)
    else:
        raise ValueError("Invalid sort key")

# Example usage
if __name__ == "__main__":
    song1 = Song(1, "Song A", "Artist X", "Genre Y")
    song2 = Song(2, "Song B", "Artist Y", "Genre X")
    song_list = [song1, song2]

    print(linear_search(song_list, 1))
    sorted_songs = sort_songs(song_list, 'artist')
    print(sorted_songs)
