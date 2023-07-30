from django.urls import path, include
from . import views
from rest_framework import urls


app_name = "users"


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('api-auth/', include('rest_framework.urls')),
]
