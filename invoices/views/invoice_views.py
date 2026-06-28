from rest_framework import viewsets
from ..serializers import InvoiceSerializer
from ..models import Person, Invoice


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        params = self.request.query_params

        buyer_id = params.get('buyerID')
        seller_id = params.get('sellerID')
        product = params.get('product')
        min_price = params.get('minPrice')
        max_price = params.get('maxPrice')
        limit = params.get('limit')

        if buyer_id:
            queryset = queryset.filter(buyer__id=buyer_id)
        if seller_id:
            queryset = queryset.filter(seller__id=seller_id)
        if product:
            queryset = queryset.filter(product__icontains=product)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if limit:
            queryset = queryset[:int(limit)]

        return queryset