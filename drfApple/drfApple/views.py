from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from Promotion.serializers import PromotionImagesSerializer
from Promotion.models import PromotionImages


@api_view()
def TestView(APIView):
    qs = PromotionImages.image.all()
    serializer = PromotionImagesSerializer(qs, many=True)
    return Response(serializer.data)
