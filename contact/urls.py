# Imports standard libraries
#...

# Imports core Django libraries
from django.urls import path

# Imports third-party libraries


# Imports from your apps
from contact.views import ContactListView, ContactCreateView, ContactDetailView, ContactUpdateView, ContactDestroyView


urlpatterns = [
    path('list-contacts', ContactListView.as_view(), name='contact-list-create'),
    path('create-contacts', ContactCreateView.as_view(), name='contact-create'),
    path('update-contacts/<int:pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('delete-contacts/<int:pk>', ContactDestroyView.as_view(), name='contact-delete'),
    path('retrieve-contacts/<int:pk>', ContactDetailView.as_view(), name='contact-retrieve'),
]
