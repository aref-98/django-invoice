from rest_framework import viewsets
from ..serializers import InvoiceSerializer
from ..models import Person, Invoice


class InvocieViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer