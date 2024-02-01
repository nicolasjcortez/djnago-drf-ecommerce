import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db

class TestCategoryModels:

    def test_str_method(self, category_factory):
        # Arrange

        # Act
        x = category_factory(name='test_cat')

        # Assert
        assert x.__str__() == 'test_cat'

class TestBrandModels:

    def test_str_method(self, brand_factory):
        # Arrange

        # Act
        x = brand_factory(name='test_bra')

        # Assert
        assert x.__str__() == 'test_bra'

class TestProductModels:
    
    
    def test_str_method(self, product_factory):
        # Arrange

        # Act
        x = product_factory(name='test_pro')

        # Assert
        assert x.__str__() == 'test_pro'

class TestProductLineModels:
    
    
    def test_str_method(self, product_line_factory):
        # Arrange

        # Act
        x = product_line_factory(sku='test_pro')

        # Assert
        assert x.__str__() == 'test_pro'

    def test_duplicated_order_values(self, product_line_factory, product_factory):
        # Arrange
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        
        # Act, Assert
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()
        

        