from rest_framework import serializers

from store.models import Product, Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    parent = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Review
        fields = ("id", "user", "title", "content", "parent", "product")


class ProductsListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    producer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewCreateSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "name", "weight", "shelf_time", "price", "photo", "discount", "is_available", "producer",
                  "category", 'reviews')
