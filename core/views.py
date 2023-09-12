from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Author, Category, PublishingCompany


class CategorySerializer(ModelSerializer):
    """Serializer class that serializes data from the Category model."""

    class Meta:
        model = Category
        fields = "__all__"


class CategoryView(APIView):
    """View class that retrieves data from the Category model and returns it as a JSON response."""

    def get(self, _):
        """Retrieves data from the Category model and returns it as a JSON response.

        Parameters:
        - _: The HTTP request object.

        Returns:
        - HttpResponse: The formatted data as a JSON response.
        """
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new category.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: The HTTP response object containing the newly created category data.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CategoryDetailView(APIView):
    """View class that retrieves data from the Category model and returns it as a JSON response."""

    def get(self, _, category_id):
        """Retrieves data from the Category model and returns it as a JSON response.

        Args:
            _ (HttpRequest): The HTTP request object.
            category_id (int): The category ID.

        Returns:
            Response: The HTTP response object containing the category data.
        """
        category = get_object_or_404(Category.objects.all(), id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        """Updates a category.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The category ID.

        Returns:
            Response: The HTTP response object containing the updated category data.
        """
        category = get_object_or_404(Category.objects.all(), id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, _, category_id):
        """Deletes a category.

        Args:
            _ (HttpRequest): The HTTP request object.
            category_id (int): The category ID.

        Returns:
            Response: The HTTP response object containing the deleted category data.
        """
        category = get_object_or_404(Category.objects.all(), id=category_id)
        category.delete()
        return Response(status=204)


class AuthorSerializer(ModelSerializer):
    """Serializer class that serializes data from the Author: Firstname Lastname."""

    class Meta:
        model = Author
        fields = "__all__"


class AuthorView(ListCreateAPIView):
    """View class that retrieves data from the Author: Firstname Lastname and returns it as a JSON response."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    """View class that retrieves data from the Author: Firstname Lastname and returns it as a JSON response."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublishingCompanySerializer(ModelSerializer):
    """Serializer class that serializes data from the PublishingCompany model."""

    class Meta:
        model = PublishingCompany
        fields = "__all__"


class PublishingCompanyViewSet(ModelViewSet):
    """View class that retrieves data from the PublishingCompany model and returns it as a JSON response."""

    queryset = PublishingCompany.objects.all()
    serializer_class = PublishingCompanySerializer
