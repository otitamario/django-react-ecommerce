# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import OrderingFilter
from api.models import Product
from api.serializers import ProductSerializer
from rest_framework import viewsets, permissions


# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [OrderingFilter]
    ordering_fields = ["name", "price", "score"]
