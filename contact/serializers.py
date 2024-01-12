# Imports standard libraries
from rest_framework import serializers

# Imports core Django libraries

# Imports third-party libraries

# Imports from your apps
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    contact serializer to serializer contact datas.
    """
    class Meta:
        model = Contact
        fields = ('contact_name', 'email', 'phone', 'created_at', 'last_updated_at', 'version', 'created_by', 'updated_by')