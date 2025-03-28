from abc import ABC, abstractmethod

class Media(ABC):
    """Abstract class representing a Media
    
    Attributes:
        title (str): title of media
        release_year (int): release year of the media
    """
    def __init__(self, title : str, release_year : int):
        """Constructor for abstract class Media

        Parameters:
            title (str): title of media
            release_year (int): release year of the media
        """
        self._title = title
        self._release_year = release_year

    @abstractmethod
    def display_info(self):
        pass

    def to_dict(self):
        """Create a dictionnary representation of Media object
        """
        return { 'title' : self._title, 'release_year' : self._release_year }
    
    def from_dict(self, data : dict):
        """Modify a Media using dictionnary data
        """
        if data['title'] and data['release_year']:
            self._title = data['title']
            self._release_year = data['release_year']
            return self
        else:
            return None
        
    def get_title(self):
        """Getter for title attribute
        Returns:
            str: title of Media
        """
        return self._title

    def __lt__(self, obj):
        """Comparison function for Media using release_year for sorting
        
        Params:
            obj (Media) : media object to compare with self
        """
        if self._release_year < obj._release_year:
            return True
        else:
            return False
        
    def __str__(self):
        """String representation of object Media

        Returns:
            str: string
        """
        return "Titre : " + self._title + ", Date de sortie : " + str(self._release_year)
