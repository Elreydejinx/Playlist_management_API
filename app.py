# app.py

from flask import Flask, request, jsonify
from playlist_management import Song, Playlist
from search_sort_algorithms import linear_search, sort_songs

app = Flask(__name__)


songs_db = {}
playlists_db = {}

@app.route('/songs', methods=['POST'])
def create_song():
    data = request.json
    song = Song(data['id'], data['name'], data['artist'], data['genre'])
    songs_db[song.id] = song
    return jsonify({"message": "Song created"}), 201

@app.route('/songs/<int:song_id>', methods=['PUT'])
def update_song(song_id):
    if song_id not in songs_db:
        return jsonify({"message": "Song not found"}), 404
    data = request.json
    song = songs_db[song_id]
    song.name = data.get('name', song.name)
    song.artist = data.get('artist', song.artist)
    song.genre = data.get('genre', song.genre)
    return jsonify({"message": "Song updated"}), 200

@app.route('/songs/<int:song_id>', methods=['DELETE'])
def delete_song(song_id):
    if song_id not in songs_db:
        return jsonify({"message": "Song not found"}), 404
    del songs_db[song_id]
    return jsonify({"message": "Song deleted"}), 200

@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = songs_db.get(song_id)
    if not song:
        return jsonify({"message": "Song not found"}), 404
    return jsonify({
        "id": song.id,
        "name": song.name,
        "artist": song.artist,
        "genre": song.genre
    }), 200

@app.route('/playlists', methods=['POST'])
def create_playlist():
    data = request.json
    playlist = Playlist(data['name'])
    playlists_db[data['name']] = playlist
    return jsonify({"message": "Playlist created"}), 201

@app.route('/playlists/<string:name>', methods=['GET'])
def get_playlist(name):
    playlist = playlists_db.get(name)
    if not playlist:
        return jsonify({"message": "Playlist not found"}), 404
    return jsonify({
        "name": playlist.name,
        "songs": [{"id": song.id, "name": song.name} for song in playlist.songs]
    }), 200

@app.route('/playlists/<string:name>', methods=['PUT'])
def update_playlist(name):
    if name not in playlists_db:
        return jsonify({"message": "Playlist not found"}), 404
    data = request.json
    playlist = playlists_db[name]
    playlist.name = data.get('name', playlist.name)
    return jsonify({"message": "Playlist updated"}), 200

@app.route('/playlists/<string:name>', methods=['DELETE'])
def delete_playlist(name):
    if name not in playlists_db:
        return jsonify({"message": "Playlist not found"}), 404
    del playlists_db[name]
    return jsonify({"message": "Playlist deleted"}), 200

@app.route('/playlists/<string:name>/add_song', methods=['POST'])
def add_song_to_playlist(name):
    if name not in playlists_db:
        return jsonify({"message": "Playlist not found"}), 404
    data = request.json
    song = songs_db.get(data['id'])
    if not song:
        return jsonify({"message": "Song not found"}), 404
    playlists_db[name].add_song(song)
    return jsonify({"message": "Song added to playlist"}), 200

@app.route('/playlists/<string:name>/remove_song', methods=['POST'])
def remove_song_from_playlist(name):
    if name not in playlists_db:
        return jsonify({"message": "Playlist not found"}), 404
    data = request.json
    playlists_db[name].remove_song(data['id'])
    return jsonify({"message": "Song removed from playlist"}), 200

@app.route('/playlists/<string:name>/sort_songs', methods=['POST'])
def sort_playlist_songs(name):
    if name not in playlists_db:
        return jsonify({"message": "Playlist not found"}), 404
    data = request.json
    key = data.get('key', 'name')
    playlists_db[name].sort_songs(key)
    return jsonify({"message": "Playlist sorted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
