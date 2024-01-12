# Imports standard libraries
from django.shortcuts import render

# Imports core Django libraries
from django.contrib.auth import authenticate  

# Imports third-party libraries
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication  
from rest_framework.permissions import IsAuthenticated  

# Imports from your apps
from .models import Contact
from .serializers import ContactSerializer



class ContactListView(generics.ListAPIView):
    """
    list all contact in db 
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactCreateView(generics.CreateAPIView):
    """
    create new contact in db
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class ContactDetailView(generics.RetrieveAPIView):
    """
    get contact by id 
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactUpdateView(generics.UpdateAPIView):
    """ 
    update contact by id
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDestroyView(generics.DestroyAPIView):
    """
    delete contact by id
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer