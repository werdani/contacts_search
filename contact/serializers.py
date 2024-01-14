# Imports standard libraries
from rest_framework import serializers

import time
from django.db import transaction
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
        fields = ('contact_name', 'email', 'phone', 'created_at', 'last_updated_at', 'created_by', 'updated_by')
    
    def update(self, instance, validated_data):
        with transaction.atomic():
            Contact.objects.select_for_update().get(id=instance.id)
            # time.sleep(50)  ## for testing 
            return super().update(instance, validated_data)
