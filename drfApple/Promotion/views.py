# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Promotion.serializers import PromotionImagesSerializer
from Promotion.models import PromotionImages


@api_view()
def TestView(request):
    qs = PromotionImages.objects.all()
    serializer = PromotionImagesSerializer(qs, many=True)
    return Response(serializer.data)
