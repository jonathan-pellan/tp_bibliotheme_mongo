class Track():
    """
    A class representing a music Track
    
    Attributes:
        title (str): title of the track
        length(int): duration of track (in seconds)
    """
        
    def __init__(self, title : str, length : int):
        """Initializes a Track object
        
        Parameters:
            title (str): title of track
            length (int): duration of track in seconds
        """
        self.__title = title
        self.__length = length

    def to_dict(self):
        """Create a dictionnary representation of Track object
        
        Returns:
            dict: dictionnary of attributes from Track object
        """
        return { 'title' : self.__title, 'length' : self.__length }
    
    def __str__(self):
        """String representation of object Movie

        Returns:
            str: string
        """
        return "Titre : " + self.__title + ", Longueur : " + str(self.__length)