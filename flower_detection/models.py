from django.db import models

class Info(models.Model):
    flower_name = models.CharField(max_length=100)
    introduction = models.TextField()
    etymology = models.TextField()
    evolution = models.TextField()
    species = models.TextField()
    tax_domain = models.CharField(max_length=100)
    tax_kingdom = models.CharField(max_length=100)
    tax_phylum = models.CharField(max_length=100)
    tax_order = models.CharField(max_length=100)
    tax_family = models.CharField(max_length=100)
    tax_genus = models.CharField(max_length=100)
    ornamental_plants = models.TextField()
    cut_flowers = models.TextField()
    medicinal_uses = models.TextField()
    health_benefits = models.TextField()
    perfumes_food = models.TextField()
    symbolizes = models.TextField()
    season_to_grow = models.TextField()
    
    def __str__(self):
        return self.flower_name 

class Uploaded_Image(models.Model):
    uploaded_image = models.ImageField(blank=False, upload_to="User_uploaded_images/")

    def filen(self):
        path = self.image.path