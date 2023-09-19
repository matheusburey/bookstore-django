from rest_framework.viewsets import ModelViewSet

from core.models import PublishingCompany
from core.serializers import PublishingCompanySerializer


class PublishingCompanyViewSet(ModelViewSet):
    """View class that retrieves data from the PublishingCompany
    model and returns it as a JSON response."""

    queryset = PublishingCompany.objects.all()
    serializer_class = PublishingCompanySerializer
