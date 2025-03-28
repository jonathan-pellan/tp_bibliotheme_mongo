from models.media import Media

class Book(Media):
    """A class representing a book
    
    Attributes:
        title (str): title of the book
        release_year (int): year of book release
        author (str): author of the book
        pages (int): number of pages in the book
    """
    def __init__(self, title : str, release_year : int, author : str, pages : int):
        """Initializes a Book object

        Parameters:
            title (str): title of book
            release_year (int): year of book release
            author (str): book author
            pages (int): number of pages in book
        """
        super().__init__(title, release_year)
        self.__author = author
        self.__pages = pages
    
    def display_info(self):
        return super().display_info()
    
    def to_dict(self):
        """Create a dictionnary representation of Book object
        
        Returns:
            dict: dictionnary of attributes from Book object
        """
        book_dict = super().to_dict()
        book_dict['author'] = self.__author
        book_dict['pages'] = self.__pages
        return book_dict
    
    # def from_dict(self, data):
    #     return super().from_dict(data)
    
    def __str__(self):
        """String representation of object Book

        Returns:
            str: string
        """
        return super().__str__() + ", Auteur : " + self.__author + ", Pages : " + str(self.__pages)