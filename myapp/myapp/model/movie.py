from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer
from sqlalchemy.orm import relation, backref

from myapp.model import DeclarativeBase, metadata, DBSession

__all__ = ['Movie', 'Genre', 'Cast']

movie_genre_table = Table('movie_genre', metadata,
    Column('movie_id', Integer, ForeignKey('movies.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


class Movie(DeclarativeBase):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255))
    director = Column(Unicode(255))


class Genre(DeclarativeBase):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255))
    movies = relation('Movie', secondary=movie_genre_table, backref='genres')

    def __unicode__(self):
        return unicode(self.name)


class Cast(DeclarativeBase):
    __tablename__ = 'casts'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id))
    movie = relation(Movie, backref=backref('cast'))
    character = Column(Unicode(255))
    actor = Column(Unicode(255))
