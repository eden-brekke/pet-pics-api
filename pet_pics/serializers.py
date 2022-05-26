from rest_framework import serializers
from .models import PetPic

class PetSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'type_of_pet', 'description', 'img', 'added_by')
    model = PetPic