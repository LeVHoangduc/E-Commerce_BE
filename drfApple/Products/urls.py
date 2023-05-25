from django.urls import path
from . import views


urlpatterns = [
    path("productList", views.ProductList.as_view(), name="product-list"),
]
