import factory

from drfecommerce.product.models import Brand, Category, Product, ProductLine


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
    is_active = True

class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine
        
    price = 10
    sku = factory.Sequence(lambda n: f'product_line_{n}')
    stock_qty = 10
    product = factory.SubFactory(ProductFactory)
    is_active = True