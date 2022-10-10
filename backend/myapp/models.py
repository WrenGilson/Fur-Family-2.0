from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=200, default="name")
    animalType = models.CharField(max_length=200, default="type")
    breed = models.CharField(max_length=200, default="breed")
    adoptionYear = models.IntegerField(default="2022")
    color = models.CharField(max_length=200, default="color")
    description = models.CharField(max_length=200, default="Good boy")



# p = Pet(name="Gwen",animalType="cat",breed="American medium-hair",adoptionYear=2016,color="black and white",description="Gwen is persnickety and particular. She likes long cat naps and scratching things--including hands. Her favorite person is her dad. She loves drinking straight from the faucet.")