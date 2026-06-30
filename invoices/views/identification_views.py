from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import InvoiceSerializer
from ..models import Invoice


@api_view(['GET'])
def sales_by_identification(request, ico):
    invoices = Invoice.objects.filter(seller__identificationNumber=ico)
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def purchases_by_identification(request, ico):
    invoices = Invoice.objects.filter(buyer__identificationNumber=ico)
    serializer = InvoiceSerializer(invoices, many=True)
    return Response(serializer.data)