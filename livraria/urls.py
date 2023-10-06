from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core import views

router = routers.DefaultRouter()

router.register(r"publishing_company", views.PublishingCompanyViewSet)
router.register(r"book", views.BookViewSet)
router.register(r"order", views.OrderViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/category/", views.CategoryView.as_view()),
    path("api/category/<int:category_id>", views.CategoryDetailView.as_view()),
    path("api/author/", views.AuthorView.as_view()),
    path("api/author/<int:pk>", views.AuthorDetailView.as_view()),
    path("api/", include(router.urls)),
]
