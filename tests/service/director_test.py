import pytest
from tests.dao.director_mock import director_dao
from service.director import DirectorService


class TestDirector:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_one(self):
        model = self.director_service.get_one(1)

        assert model is not None
        assert model.id is not None

    def test_get_all(self):
        models = self.director_service.get_all()
        assert len(models) > 0

    def test_create(self):
        data = {
            "id": 3,
            "name": "Foo"
        }
        model = self.director_service.create(data)

        assert model is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        data = {
            "id": 3,
            "name": "Foo"
        }
        self.director_service.update(data)
