from django.db import models
from cities_light.models import City
from django.contrib.auth.models import User


class Profile(models.Model):
    OPTION_ONE = 'yesterday'
    OPTION_TWO = 'last week'
    OPTION_THREE = 'last mounth'

    OPTION_CHOICES = [
        (OPTION_ONE, 'yesterday'),
        (OPTION_TWO, 'last week'),
        (OPTION_THREE, 'last mounth'),
    ]



    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    City=models.ForeignKey(City,on_delete=models.SET_NULL,null=True,blank=True,related_name='City')
    FirstName=models.CharField(max_length=100 ,blank=True)
    LastName=models.CharField(max_length=100 ,blank=True)
    Email=models.EmailField(blank=True)
    Picture=models.ImageField(null=True,blank=True, upload_to='images/' )
    date_of_search = models.CharField(
        max_length=20,
        choices=OPTION_CHOICES,
        default=OPTION_ONE,
    )
    def __str__(self):
        return f"owend by {self.user}"
