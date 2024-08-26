from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, TripSerializer, ItinerarySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Trip, Itinerary

#--------------------------------#
# TRIPS
#--------------------------------#

class TripListCreate(generics.ListCreateAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

class TripDelete(generics.DestroyAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(user=user)
    
class TripRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = TripSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Trip.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

#--------------------------------#
# ITINERARIES
#--------------------------------#

class ItineraryListCreate(generics.ListCreateAPIView):
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        trip_id = self.kwargs.get('pk')
        return Itinerary.objects.filter(trip_id=trip_id)
    
    def perform_create(self, serializer):
        trip_id = self.kwargs.get('pk')
        trip = Trip.objects.get(id=trip_id)
        if serializer.is_valid():
            serializer.save(trip=trip)
        else:
            print(serializer.errors)

class ItineraryDelete(generics.DestroyAPIView):
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Itinerary.objects.filter(user=user)
    
class ItineraryRetrieveUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Itinerary.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
