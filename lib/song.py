class Song:
    genres = []
    artists = []
    count = 0
    genre_count = {}
    
    
    def __init__( self, name, artist, genre ) :

        self.name = name
        self.artist = artist
        self.genre = genre
        
        self.add_song_count()
        self.add_genre()
        self.add_artist()
    
    @classmethod
    def add_song_count( cls ):

        cls.count += 1
    
    @classmethod
    def add_genre( cls ) :

        if cls.genre not in cls.genres:
            cls.genres.append( cls.genre )
            cls.add_to_genre_count()
    
    @classmethod
    def add_artist( cls ) :

        if cls.artist not in cls.artists:
            cls.artists.append( cls.artist )
    
    @classmethod
    def add_to_genre_count( cls ) :

        if cls.genre in cls.genre_count:
            cls.genre_count[ cls.genre ] += 1
        else:
            cls.genre_count[ cls.genre ] = 1