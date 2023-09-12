from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from core.models import Category


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
        - request: The HTTP request object.

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
