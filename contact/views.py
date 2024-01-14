# Imports standard libraries
from django.shortcuts import render

# Imports core Django libraries
from django.contrib.auth import authenticate  

# Imports third-party libraries
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response
from rest_framework import status

# Imports from your apps
from .models import Contact
from .serializers import ContactSerializer



class ContactListView(generics.ListAPIView):
    """
    list all contact in db 
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    """
    create new contact in db
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer


class ContactDetailView(generics.RetrieveAPIView):
    """
    get contact by id 
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer

class ContactUpdateView(generics.UpdateAPIView):
    """ 
    update contact by id
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.version != int(request.data.get('version', 0)):
            return Response({'error': 'Conflict - Contact has been updated by another user.'}, status=status.HTTP_409_CONFLICT)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class ContactDestroyView(generics.DestroyAPIView):
    """
    delete contact by id
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer