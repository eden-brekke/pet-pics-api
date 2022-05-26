from django.urls import path
from .views import PetPicList, PetPicDetail


urlpatterns = [
  path('', PetPicList.as_view(), name="pet_list"),
  path('<int:pk>/', PetPicDetail.as_view(), name="pet_detail"),
]