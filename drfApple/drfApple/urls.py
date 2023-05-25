from django.contrib import admin
from django.urls import path, include
from .views import TestView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Promotion.urls")),
    path("", include("Products.urls")),
]
