from django.urls import path
from core.views import home_view, HomeView, ProductDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="store"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product-details")
]
