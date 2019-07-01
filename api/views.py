from django.shortcuts import render

from rest_framework import viewsets

from workout.models import Rep, Set, Workout
from api.serializers import RepSerializer, SetSerializer, WorkoutSerializer

class RepViewSet(viewsets.ModelViewSet):
    queryset = Rep.objects.all()
    serializer_class = RepSerializer


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
