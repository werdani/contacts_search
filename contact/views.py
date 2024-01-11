#Imports standard libraries
from django.shortcuts import render

# Imports core Django libraries
#... 

#Imports third-party libraries
from rest_framework import generics


# Imports from your apps
from .models import Contact
from .serializers import ContactSerializer


class ContactView(generics.ListCreateAPIView):
    """
    list all contact in db 
    create new contact in db
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get contact by id 
    update contact by id
    delete contact by id
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

