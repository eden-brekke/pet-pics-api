from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class PetPic(models.Model):
    name = models.CharField(max_length=256)
    type_of_pet = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    img = models.URLField(max_length=256)
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name