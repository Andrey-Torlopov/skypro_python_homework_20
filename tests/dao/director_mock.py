import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO

@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    models = [
        Director(id=1, name="Jhon"),
        Director(id=2, name="Jane")
    ]

    director_dao.create = MagicMock(return_value=Director(id=3, name="Foo"))
    director_dao.delete = MagicMock()
    director_dao.get_one = MagicMock(return_value=models[0])
    director_dao.get_all = MagicMock(return_value=models)
    director_dao.update = MagicMock()

    return director_dao
