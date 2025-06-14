from django.db import models
from django.contrib.auth.models import User
from datetime import  timedelta,date
from cities_light.models import Country
from django.utils import timezone
import pytz


class TaskList(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'owend by {self.owner}'

class Task(models.Model):
    TASK_PREIORETY = (
        ('H', 'high'),
        ('M', 'medium'),
        ('L', 'low'),
    )
    list=models.ForeignKey(TaskList,on_delete=models.CASCADE,null=True)
    text=models.TextField(blank=True)
    status=models.BooleanField(default=False)
    Preiorety=models.CharField( 
        max_length=1,
        choices=TASK_PREIORETY ,
        default='M'
    )
    start_date=models.DateField(auto_now_add=True)
    deadline=models.DateField(
        default=date.today()+timedelta(days=7),
        )
    class Meta:
        ordering= ['Preiorety']

    def __str__(self):
        return f"{self.text[0:15]}..." 

def get_default_country():
    try:
        return Country.objects.first().id
    except:
        return None

default_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, default=get_default_country)
class CountryList(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    country_1=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country_1',default=default_country)
    country_2=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country_2',default=default_country)
    country_3=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country_3',default=default_country)
    country_4=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='country_4',default=default_country)
    def get_gmc_time(country):
        country_timezone=pytz.timezone(country.timezone)
        country_time=timezone.now().astimezone(country_timezone)
        gms_time=country_time.astimezone(pytz.utc)
        return gms_time
    def __str__(self):
        return f'owend by {self.owner}'
