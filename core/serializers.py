from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Author, Book, Category, Order, PublishingCompany


class CategorySerializer(ModelSerializer):
    """Serializer class that serializes data from the Category model."""

    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    """Serializer class that serializes data from the Author: Firstname Lastname."""

    class Meta:
        model = Author
        fields = "__all__"


class PublishingCompanySerializer(ModelSerializer):
    """Serializer class that serializes data from the PublishingCompany model."""

    class Meta:
        model = PublishingCompany
        fields = "__all__"


class BookSerializer(ModelSerializer):
    """Serializer class that serializes data from the Book model."""

    category = SerializerMethodField()
    authors = SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

    def get_category(self, obj):
        """Get the category of an object.

        Returns:
            str: The description of the category.
        """
        return obj.category.description

    def get_authors(self, obj):
        authors = obj.authors.all()
        return [author.name for author in authors]


class OrderSerializer(ModelSerializer):
    """Serializer class that serializes data from the Order model."""

    client = SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_client(self, obj):
        """Get the user of an object."""
        return obj.client.name
