import json

import pytest

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(4)

        # Act
        response = api_client().get(self.endpoint)

        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

class TestBrandEndpoints:

    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(3)

        # Act
        response = api_client().get(self.endpoint)

        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3


class TestProductEndpoints:

    endpoint = "/api/product/"

    def test_get_all(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(5)

        # Act
        response = api_client().get(self.endpoint)

        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5

    def test_get_single_product_by_slug(self, product_factory, api_client):
        # Arrange
        obj = product_factory(slug="test_slug")

        # Act
        response = api_client().get(f"{self.endpoint}{obj.slug}/")

        # Assert
        assert response.status_code == 200

    def test_get_products_by_category_slug(self, category_factory, product_factory, api_client):
        # Arrange
        obj = category_factory(slug="cat-test")
        product_factory(category=obj)

        # Act
        response = api_client().get(f"{self.endpoint}category/{obj.slug}/")

        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

        
