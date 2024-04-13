from pyexpat import model
from unicodedata import category
from django.db import models
from django.urls import reverse, reverse_lazy
# Create your models here.

class Drug(models.Model):
    DRUG_CATEGORY = (
        ('Syrup', 'Syrup'),
        ('Tablet', 'Tablet'),
        ('Injection', 'Injection'),
        ('Capsule', 'Capsule'),
        ('Caplet', 'Caplet'),
        ('Powder', 'Powder'),
    )
    # pharm_id = models.ForeignKey(Pharmacy, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices= DRUG_CATEGORY)
    maufacturer = models.CharField(max_length=150)
    photo = models.FileField(max_length=500, upload_to='drugs')
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manageDrug')

class Pharmacy(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    services = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    location = models.CharField(max_length=200)
    founder = models.CharField(max_length=500)
    facebook = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=100)
    description = models.TextField()
    About = models.TextField()
    logo = models.FileField(upload_to='Pharmacy_logo')
    image1 = models.FileField(upload_to='PharmacyImage')
    image2 = models.FileField(upload_to='PharmacyImage')
    drugs = models.ManyToManyField(Drug)
    class Meta:
        verbose_name_plural = 'Pharmacy'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('managePharmacy')

