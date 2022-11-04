import pytest
from unittest.mock import MagicMock
from dao.model.genre import Genre
from dao.genre import GenreDAO


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    models = [
        Genre(id=1, name="Jhon"),
        Genre(id=2, name="Jane")
    ]

    genre_dao.create = MagicMock(return_value=Genre(id=3, name="Foo"))
    genre_dao.delete = MagicMock()
    genre_dao.get_one = MagicMock(return_value=models[0])
    genre_dao.get_all = MagicMock(return_value=models)
    genre_dao.update = MagicMock()

    return genre_dao
