from rest_framework.response import Response


from Products.serializers import ProductSerializer
from Products.models import Product

from rest_framework import generics


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #  configure the data model
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "message": "Lấy các sản phẩm thành công",
            "data": {"products": serializer.data},
        }
        return Response(data)
