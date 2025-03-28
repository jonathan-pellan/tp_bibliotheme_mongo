from models.media import Media
from models.book import Book
from models.movie import Movie
from models.album import Album
from models.track import Track
import pymongo

class Library():
    """A class representing a Library
    
    Attributes:
        medias (list[Media]): a list of Media objects that is contained in Library
    """
    def __init__(self, medias : list[Media]):
        """Initializes a Library object

        Parameters:
            medias (list[Media]): list of media
        """
        self.__medias = medias

    def add_media(self, media : Media):
        """Method for adding a media inside a Library
        
        Parameters:
            media (Media): media to add
        """
        self.__medias.append(media)

    def remove_media(self, title : str):
        """Method for deleting a media from a Library
        
        Parameters:
            title (str): title of media to delete from Library
        """
        media_to_remove = None
        for media in self.__medias:
            if media.get_title() == title:
                media_to_remove = media
        if media_to_remove:
            self.__medias.remove(media)

    def search(self, keyword : str):
        """Method for searching a media by keyword inside a Library
        
        Parameters:
            keyword (str): keyword to match with a the content of a title
            
        Returns:
            str: list of Media matching the keyword"""
        list_medias = []
        for media in self.__medias:
            if keyword.lower() in media.get_title().lower():
                list_medias.append(media)
        return list_medias
    
    def list_media(self, order_by : str):
        """Method for sorting Library
        
        Parameters:
            order_by (str): ["title","year"] sort by title or year
        """
        if order_by == 'title':
            return sorted(self.__medias, key=lambda x : x.get_title())
        elif order_by == 'year':
            return sorted(self.__medias)
        
    def display_all(self):
        pass

    def save_to_mongo(self):
        pass
        
    def load_from_mongo(self):
        """Method for loading a collection of documents containing medias into a Library object
        
        Returns:
            Library: a Library object containing media from MongoDB"""
        client = pymongo.MongoClient('localhost', 27017)
        db = client['media_library']
        library = db['library']
        for media in library.find(filter={"author" : {"$exists" : True}}, projection={'_id' : False}):
            book = Book(**media)
            self.add_media(book)
        for media in library.find({"director" : {"$exists" : True}}, projection={'_id' : False}):
            movie = Movie(**media)
            self.add_media(movie)
        for media in library.find({"artist" : {"$exists" : True}}, projection={'_id' : False}):
            track_list = []
            for m in media['tracks']:
                track = Track(**m)
                track_list.append(track)
            album_dict = media
            album_dict['tracks'] = track_list
            album = Album(**album_dict)
            self.add_media(album)
        return self