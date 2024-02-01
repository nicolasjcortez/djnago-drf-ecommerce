from django.db import connection
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple View set to view all categories
    """

    queryset = Category.objects.all()

    @extend_schema(tags=['category'],responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    """
    A simple View set to view all brands
    """

    queryset = Brand.objects.all()


    @extend_schema(tags=['brand'],responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple View set to view all product
    """

    queryset = Product.objects.is_active()

    

    lookup_field = "slug"

    @extend_schema(tags=['product'],responses=ProductSerializer)
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset
                                       .filter(slug=slug)
                                       .select_related("category", "brand"), 
                                       many=True)
        data = Response(serializer.data)

        q = list(connection.queries)
        print(len(q))
        for qs in q:  
            print(highlight(str(qs["sql"]), SqlLexer(), TerminalFormatter()))
        
        
        return data


    @extend_schema(tags=['product'],responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(tags=['product'], responses=ProductSerializer)
    @action(methods=['get'], detail=False, url_path=r"category/(?P<slug>[\w-]+)")
    def list_product_by_category_slug(self, request, slug=None):
        """
        An endpoint to return product by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__slug=slug), many=True)
        return Response(serializer.data)