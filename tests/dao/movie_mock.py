import pytest
from unittest.mock import MagicMock
# from dao.model.movie import Movie
from dao.movie import MovieDAO, Movie


@pytest.fixture()
def movie_dao():
    dao = MovieDAO(None)

    models = [
        Movie(
            id=1,
            title="FooTitle",
            description="Foo description",
            trailer="Foo trailer",
            year=2000,
            rating="R",
            genre_id=1,
            director_id=1
        ),
        Movie(
            id=2,
            title="FooTitle 2",
            description="Foo description 2",
            trailer="Foo trailer 2",
            year=2001,
            rating="R",
            genre_id=2,
            director_id=2
        )
    ]

    created_movie = Movie(
        id=3,
        title="FooTitle 3",
        description="Foo description 3",
        trailer="Foo trailer 3",
        year=2003,
        rating="R",
        genre_id=1,
        director_id=1
    )

    dao.create = MagicMock(return_value=created_movie)
    dao.delete = MagicMock()
    dao.get_one = MagicMock(return_value=models[0])
    dao.get_all = MagicMock(return_value=models)
    dao.update = MagicMock()

    return dao
