from django.urls import path
from . import views

urlpatterns = [
    # trips
    path('trips/', views.TripListCreate.as_view(), name='trip-list'),
    path('trip/delete/<int:pk>/', views.TripDelete.as_view(), name='delete-trip'),
    path('trip/update/<int:pk>/', views.TripRetrieveUpdate.as_view(), name='update-trip'),

    # itineraries
    path('itineraries/', views.ItineraryListCreate.as_view(), name='itinerary-list'),
    path('itinerary/delete/<int:pk>/', views.ItineraryDelete.as_view(), name='delete-itinerary'),
    path('itinerary/update/<int:pk>/', views.ItineraryRetrieveUpdate.as_view(), name='update-itinerary'),
]