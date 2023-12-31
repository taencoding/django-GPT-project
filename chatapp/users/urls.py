from django.urls import path, include
from . import views
from rest_framework import urls

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "users"


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls')),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
