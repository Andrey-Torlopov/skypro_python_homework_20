import pytest
from tests.dao.movie_mock import movie_dao
from service.movie import MovieService


class TestMovie:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_one(self):
        model = self.movie_service.get_one(1)

        assert model is not None
        assert model.id is not None

    def test_get_all(self):
        models = self.movie_service.get_all()
        assert len(models) > 0

    def test_create(self):
        data = {
            "id": 3,
            "title": "FooTitle 3",
            "description": "Foo description 3",
            "trailer": "Foo trailer 3",
            "year": 2003,
            "rating": "R",
            "genre_id": 1,
            "director_id": 1
        }
        model = self.movie_service.create(data)

        assert model is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        data = {
            "id": 3,
            "title": "FooTitle 3",
            "description": "Foo description 3",
            "trailer": "Foo trailer 3",
            "year": 2003,
            "rating": "R",
            "genre_id": 1,
            "director_id": 1
        }
        self.movie_service.update(data)
