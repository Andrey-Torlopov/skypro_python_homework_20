import pytest
from tests.dao.genre_mock import genre_dao
from service.genre import GenreService


class TestGenre:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_one(self):
        model = self.genre_service.get_one(1)

        assert model is not None
        assert model.id is not None

    def test_get_all(self):
        models = self.genre_service.get_all()
        assert len(models) > 0

    def test_create(self):
        data = {
            "id": 3,
            "name": "Foo"
        }
        model = self.genre_service.create(data)

        assert model is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        data = {
            "id": 3,
            "name": "Foo"
        }
        self.genre_service.update(data)
