from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
DestroyAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.views import APIView

from .models import *
from .serializers import *

class ListCreateSpecAPIView(ListCreateAPIView):     # создает спец и отображает всех
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    
class RetrieveSpecAPIView(RetrieveAPIView):       # отображает одного по ID
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DestroySpecAPIView(DestroyAPIView):          # удаляет по ID
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class UpdateSpecAPIView(UpdateAPIView):          # обновление по ID
    queryset = Specialization.objects.all()         # put полное изменение
    serializer_class = SpecializationSerializer         # patch частичное изменение