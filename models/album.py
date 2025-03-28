from models.media import Media
from models.track import Track

class Album(Media):
    """A class representing a music album
    
    Attributes:
        title (str): the title from the album
        release_year (int): year of album release
        artist (str): album's artist
        tracks (list[Track]): list of tracks contained in album
    """
    def __init__(self, title : str, release_year : int, artist : str, tracks : list[Track]):
        """Initializes an Album object

        Parameters:
            title (str): title of album
            release_year (int): year of album release
            artist (str): album artist
            tracks (list[Track]): list of tracks (Track objects) contained in album
        """
        super().__init__(title, release_year)
        self.__artist = artist
        self.__tracks = tracks

    def display_info(self):
        return super().display_info()
    
    def to_dict(self):
        """Create a dictionnary representation of Album object
        
        Returns:
            dict: dictionnary of attributes from Album object
        """
        album_dict = super().to_dict()
        album_dict['artist'] = self.__artist
        track_dict = []
        for track in self.__tracks:
            track_dict.append(track.to_dict())
        album_dict['tracks'] = track_dict
        return album_dict

    # def from_dict(self, data):
    #     return super().from_dict(data)

    def __str__(self):
        """String representation of object Album

        Returns:
            str: string
        """
        string = super().__str__() + ", Artiste : " + self.__artist + "\nPistes : "
        for track in self.__tracks:
            string += "\n"
            string += str(track)
        return string
                
    def __len__(self):
        """Method len for album object
        
        Returns:
            int: number of tracks in album
        """
        return len(self.__tracks)