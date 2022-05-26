from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import PetPic


class PetPicTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_pet_pic = PetPic.objects.create(
            name="Pumpkin",
            added_by=testuser1,
            description="Best baby kitty gorl",
        )
        test_pet_pic.save()

    def test_pet_pic_model(self):
        pet = PetPic.objects.get(id=1)
        actual_added_by = str(pet.added_by)
        actual_name = str(pet.name)
        actual_description = str(pet.description)
        self.assertEqual(actual_added_by, "testuser1")
        self.assertEqual(actual_name, "Pumpkin")
        self.assertEqual(
            actual_description, "Best baby kitty gorl"
        )

    def test_get_pet_pic_list(self):
        url = reverse("pet_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pets = response.data
        self.assertEqual(len(pets), 1)
        self.assertEqual(pets[0]["name"], "Pumpkin")

    def test_get_pet_pic_by_id(self):
        url = reverse("pet_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pet = response.data
        self.assertEqual(pet["name"], "Pumpkin")

    def test_create_pet(self):
        url = reverse("pet_list")
        data = {"added_by": 1, "name": "Jack", "description": "goodest boi", "type_of_pet": "cat", "img": "https://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        pets = PetPic.objects.all()
        self.assertEqual(len(pets), 2)
        self.assertEqual(PetPic.objects.get(id=2).name, "Jack")

    def test_update_cat(self):
        url = reverse("pet_detail", args=(1,))
        data = {
            "added_by": 1,
            "name": "Jack",
            "description": "goodest boi",
            "type_of_pet": "cat",
            "img": "https://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pets = PetPic.objects.get(id=1)
        self.assertEqual(pets.name, data["name"])
        self.assertEqual(pets.added_by.id, data["added_by"])
        self.assertEqual(pets.description, data["description"])
        self.assertEqual(pets.type_of_pet, data["type_of_pet"])
        self.assertEqual(pets.img, data["img"])

    def test_delete_pet(self):
        url = reverse("pet_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        pets = PetPic.objects.all()
        self.assertEqual(len(pets), 0)