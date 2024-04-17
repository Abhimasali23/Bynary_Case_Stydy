from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('customer/', views.customer, name='customer'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('submitted/', views.request_submitted, name='request_submitted'),
    path('track_request/', views.track_request, name='track_request'),
]

