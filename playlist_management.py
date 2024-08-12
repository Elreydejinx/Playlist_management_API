
class Song:
    def __init__(self, id, name, artist, genre):
        self.id = id
        self.name = name
        self.artist = artist
        self.genre = genre

    
    def __repr__(self):
        return f"Song(id={self.id}, name='{self.name}', artist='{self.artist}', genre='{self.genre}')"
    

class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            print(f"Song '{song.name}' already exists in the playlist.")

    def remove_song(self, song_id):
        self.songs = [song for song in self.songs if song.id != song_id]

    def sort_songs(self, key='name'):
        if key == 'name':
            self.songs.sort(key=lambda x: x.name)
        elif key == 'artist':
            self.songs.sort(key=lambda x: x.artist)
        elif key == 'genre':
            self.songs.sort(key=lambda x: x.genre)

    def __repr__(self):
        return f"Playlist(name='{self.name}', songs={self.song})"
    
if __name__ == "__main__":
    song1 = Song(1, "Gimmie my bag", "Young Dolph", "Rap")
    song2 = Song(2, "Thinking out Loud", "Young Dolph", "Rap")

    playlist = Playlist("Gangsta Ish")
    playlist.add_song(song1)
    playlist.add_song(song2)

    print(playlist)
    playlist.sort_songs('artist')
    print(playlist)
    playlist.remove_song(1)
    print(playlist )