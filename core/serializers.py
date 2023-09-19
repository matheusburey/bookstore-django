from rest_framework.serializers import ModelSerializer

from core.models import Author, Book, Category, PublishingCompany


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

    class Meta:
        model = Book
        fields = "__all__"
