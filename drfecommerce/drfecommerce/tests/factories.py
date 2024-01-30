import factory

from drfecommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.Sequence(lambda n: f'category_{n}')

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        
    name = factory.Sequence(lambda n: f'brand_{n}')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "test_product"
    description = "test description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)