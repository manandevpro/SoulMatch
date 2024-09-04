from typing import Iterable
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.

class Religion(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Sect(models.Model):
    name=models.CharField(max_length=256)
    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='Sects', null=True)

    def __str__(self):
        return self.name

class Caste(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Hobby(models.Model):
    name=models.CharField(max_length=256)

    class Meta:
        verbose_name_plural="hobbies"
    
    def __str__(self):
        return self.name

class FatherProfile(models.Model):
    name=models.CharField(max_length=256)
    occupation=models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

 
class Profile(models.Model):
    GENDER_Choices=[
        ('M', 'Male'),
        ('F','Female')
        ]
    name=models.CharField(max_length=256, default="Unnamed")
    profile_pic=models.ImageField(null=True, blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_Choices)
    occupation=models.CharField(max_length=256, null=True, blank=True)
    birth_date=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    email=models.EmailField(max_length=256, unique=True)

    religion=models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='profiles', null=True)
    sect=models.ForeignKey(Sect, on_delete=models.CASCADE, related_name='profiles', null=True)
    caste=models.ForeignKey(Caste, on_delete=models.CASCADE, related_name='profiles', null=True)
    hobbies=models.ManyToManyField(Hobby, related_name='profiles')
    father=models.OneToOneField(FatherProfile, on_delete=models.CASCADE, related_name='Depandent', null=True)


    def save(self, *args, **kwargs):
        print(f"Data updated for {self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
