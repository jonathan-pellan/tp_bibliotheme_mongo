import pymongo
import click
from models.book import Book
from models.album import Album
from models.movie import Movie
from models.track import Track
from library import Library

@click.group()
def cli():
    pass

@cli.command()
@click.option('--type', type=str, help="Type of media (Movie, Album, Book)")
def add(type):
    """CLI Function for adding a Media in MongoDB
    
    Parameters:
        type (str): Either "movie", "album" or "book"
    """
    if type.lower() not in ['movie', 'album', 'book']:
        raise click.BadParameter("Type of media must be either Movie, Album or Book.")
    client = pymongo.MongoClient('localhost', 27017)
    db = client['media_library']
    library = db['library']
    title = click.prompt('Media Title', default="Unknown title")
    release_year = click.prompt('Release Year', default=1900)
    if type.lower() == 'movie':
        director = click.prompt('Director', type=str)
        duration = click.prompt('Duration', type=int)
        movie = Movie(title=title, release_year=release_year, director=director, duration=duration)
        library.insert_one(movie.to_dict())
        click.echo("Inserted movie into MongoDB :\n" + str(movie))
    elif type.lower() == 'book':
        author = click.prompt('Author', type=str)
        pages = click.prompt('Number of Pages', type=int)
        book = Book(title=title, release_year=release_year, author=author, pages=pages)
        library.insert_one(book.to_dict())
        click.echo("Inserted book into MongoDB :\n" + str(book))
    elif type.lower() == 'album':
        artist = click.prompt('Artist', type=str)
        number_of_tracks = click.prompt('Number of tracks', type=int)
        tracks = []
        for i in range(number_of_tracks):
            track_title = click.prompt(f'Title {i}', type=str)
            track_length = click.prompt(f'Duration {i}', type=int)
            track = Track(title=track_title, length=track_length)
            tracks.append(track)
        album = Album(title=title, release_year=release_year, artist=artist, tracks=tracks)
        library.insert_one(album.to_dict())
        click.echo("Inserted album into MongoDB :\n" + str(album))

@cli.command()
@click.option('--name', type=str, help="Title of media")
def delete(name):
    """CLI Function for removing a Media from MongoDB
    
    Parameters:
        name (str): Title of Media to delete in MongoDB
    """
    client = pymongo.MongoClient('localhost', 27017)
    db = client['media_library']
    library = db['library']
    deleted_media = library.find_one_and_delete({'title' : name}, projection={'_id' : False})
    click.echo("Deleted media from MongoDB :\n" + str(deleted_media))

@cli.command()
@click.option('--name', type=str, help="Title of media")
def search(name):
    """CLI Function for searching a Media inside MongoDB collection
    
    Parameters:
        name (str): Title of Media to search in MongoDB
    """
    client = pymongo.MongoClient('localhost', 27017)
    db = client['media_library']
    library = db['library']
    media = library.find_one({'title' : name})
    click.echo("Found media from MongoDB :\n" + str(media))

@cli.command()
@click.option('--order', default='title', help="'title' or 'year'")
def library(order):
    """CLI Function for printing all Media in Library collection
    
    Parameters:
        order (str): either "title" or "year" (default "title")
    """
    library = Library([])
    library.load_from_mongo()
    i = 1
    for media in library.list_media(order_by=order):
        print(f"Media number {i}")
        print(str(media))
        print("-----------------")
        i += 1

if __name__ == '__main__':
    cli()