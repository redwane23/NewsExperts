from django.db import models
from cities_light.models import City
from django.contrib.auth.models import User


class Profile(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    City=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True)
    FirstName=models.CharField(max_length=100 ,blank=True)
    LastName=models.CharField(max_length=100 ,blank=True)
    Email=models.EmailField(blank=True)
    Picture=models.ImageField(null=True,blank=True, upload_to='images/' )
    def __str__(self):
        return f"owend by {self.User}"
