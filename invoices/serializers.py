from rest_framework import serializers
from .models import Person, Invoice



class PersonSerializer(serializers.ModelSerializer):
    _id = serializers.IntegerField(source="id", read_only=True)
    identificationNumber = serializers.CharField(default=None)

    class Meta:
        model = Person
        fields = [
            'name', 'identificationNumber', 'taxNumber', 'accountNumber',
            'bankCode', 'iban', 'telephone', 'mail', 'street', 'zip',
            'city', 'country', 'note', '_id'
        ]

class InvoiceSerializer(serializers.ModelSerializer):
    buyer = PersonSerializer (read_only=True)
    seller = PersonSerializer(read_only=True)
    buyerId = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(), source='buyer', write_only=True
    )
    sellerId = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.all(), source='seller', write_only=True
    )

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoiceNumber', 'issued', 'dueDate', 'product', 'price', 'vat', 'note', 'buyer', 'seller', 'buyerId', 'sellerId'
        ]
