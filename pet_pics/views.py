from rest_framework import generics
from .serializers import PetSerializer
from .models import PetPic

class PetPicList(generics.ListCreateAPIView):
  queryset = PetPic.objects.all()
  serializer_class = PetSerializer
  
class PetPicDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = PetPic.objects.all()
  serializer_class = PetSerializer