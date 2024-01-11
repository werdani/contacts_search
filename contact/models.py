from django.db import models


class Contact(models.Model):
    """ Model for contact info """

    contact_name = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=15)
    created_at   = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name