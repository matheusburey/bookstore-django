from rest_framework.viewsets import ModelViewSet

from core.models import Book
from core.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """View class that retrieves data from the PublishingCompany
    model and returns it as a JSON response."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
