class Song:

    count = 0
    genres = []
    artists = []
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count(self)
        Song.add_to_genres(self, genre)
        Song.add_to_artists(self, artist)
        Song.add_to_genre_count(self, genre)
        Song.add_to_artist_count(self, artist)

    @classmethod
    def add_song_to_count(cls, self):
        cls.count += 1
    @classmethod
    def add_to_genres(cls, self, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, self, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls, self, genre):
        if cls.genre_count.get(genre) == None:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1
    @classmethod
    def add_to_artist_count(cls, self, artist):
        for artist in cls.artists:
            if cls.artist_count.get(artist) == None:
                cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1