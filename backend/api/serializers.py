from rest_framework import serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "score",
            "image",
        ]
