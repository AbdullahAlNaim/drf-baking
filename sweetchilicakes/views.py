from django.shortcuts import render
from .models import Cakes
from rest_framework import generics
from .serializers import CakeSerializer

# Create your views here.
class CakeShowcase(generics.ListCreateAPIView):
    queryset = Cakes.objects.all()
    serializer_class = CakeSerializer