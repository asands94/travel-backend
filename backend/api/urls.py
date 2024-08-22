from django.urls import path
from . import views

urlpatterns = [
    path('trips/', views.TripListCreate.as_view(), name='trip-list'),
    path('trip/delete/<int:pk>/', views.TripDelete.as_view(), name='delete-trip'),
]