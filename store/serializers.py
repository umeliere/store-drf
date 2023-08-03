from rest_framework import serializers

from store.models import Product, Review


class FilterReviewListSerializer(serializers.ListSerializer):
    """
    Serializer for MTTP-Tree filtering redundant queries
    """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """
    Recursive serializer for MTTP-Tree
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for review model, uses CRUD
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("user", "title", "content", "parent", "product")


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for review model for ProductsSerializer
    """
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("user", "title", "content", "product", 'children')


class ProductsSerializer(serializers.ModelSerializer):
    """
    Serializer for product model
    """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    producer = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ("name", "weight", "shelf_time", "price", "photo", "discount", "is_available", "producer",
                  "category", 'reviews')
