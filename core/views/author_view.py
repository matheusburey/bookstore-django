from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Author
from core.serializers import AuthorSerializer


class AuthorView(ListCreateAPIView):
    """View class that retrieves data from the Author: Firstname Lastname and returns it as a JSON response."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    """View class that retrieves data from the Author: Firstname Lastname and returns it as a JSON response."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
