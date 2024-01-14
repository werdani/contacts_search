# Imports standard libraries
import time
from django.db import transaction
from django.shortcuts import render
from django.db.models import F


# Imports core Django libraries
from django.contrib.auth import authenticate  

# Imports third-party libraries
from rest_framework import generics, serializers  
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


class ContactDestroyView(generics.DestroyAPIView):
    """
    delete contact by id
    """
    permission_classes = [IsAuthenticated]
    queryset           = Contact.objects.all()
    serializer_class   = ContactSerializer