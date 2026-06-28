from rest_framework import serializers
from .models import Person


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
