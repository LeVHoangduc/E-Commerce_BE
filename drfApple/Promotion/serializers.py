from rest_framework import serializers
from .models import PromotionImages


class PromotionImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionImages
        fields = "__all__"
