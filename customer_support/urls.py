from django.urls import path
from . import views


urlpatterns = [    
    path('manager/', views.manager, name='manager'),
    path('manage/', views.manage, name='manage'),
    path('update_request/<str:pk>/', views.update_request, name='update_request'),
    path('delete_request/<str:pk>/', views.delete_request, name='delete_request'),
    # path('update/<int:request_id>/', views.update_request_status, name='update_request_status'),
]