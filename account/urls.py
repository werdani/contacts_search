# Imports standard libraries
#...

# Imports core Django libraries
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Imports third-party libraries
#...

# Imports from your apps


urlpatterns = [
    # JWT for refresh token and generate token 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]