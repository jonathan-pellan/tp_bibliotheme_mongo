from models.media import Media

class Movie(Media):
    """A class representing a movie
    
    Attributes:
        title (str): title of the movie
        release_year (int): year of movie release
        director (str): director of the movie
        duration (int): duration of the movie (in minutes)
    """
    def __init__(self, title : str, release_year : int, director : str, duration : int):
        """Initializes a Movie object

        Parameters:
            title (str): title of movie
            release_year (int): year of movie release
            director (str): movie director
            duration (int): duration of movie in minutes
        """
        super().__init__(title, release_year)
        self.__director = director
        self.__duration = duration

    def display_info(self):
        return super().display_info()
    
    def to_dict(self):
        """Create a dictionnary representation of Movie object
        
        Returns:
            dict: dictionnary of attributes from Movie object
        """
        movie_dict = super().to_dict()
        movie_dict['director'] = self.__director
        movie_dict['duration'] = self.__duration
        return movie_dict
    
    # def from_dict(self, data):
    #     return super().from_dict(data)

    def __str__(self):
        """String representation of object Movie

        Returns:
            str: string
        """
        return super().__str__() + ", Réalisateur : " + self.__director + ", Durée : " + str(self.__duration)