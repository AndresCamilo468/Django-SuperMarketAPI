from django.urls import path, include

urlpatterns = [
    path('', include('supermarket_api.urls')),
]

