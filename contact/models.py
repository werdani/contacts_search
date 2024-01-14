from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    """ Model for contact info """

    contact_name = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=15)
    created_at   = models.DateTimeField(auto_now_add=True)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_created', null=True, blank=True)
    updated_by   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts_updated', null=True, blank=True)
    last_updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.contact_name