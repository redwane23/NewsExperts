from django.db import models
from django.contrib.auth.models import User
from datetime import  timedelta,date
from cities_light.models import Country


class TaskList(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f'TaskList owend by {self.owner}'

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
    def auto_delete(self):
        if self.deadline < date.today():
            self.delete()
        if self.status:
            self.delete()

    def __str__(self):
        return f"{self.text[0:15]}..." 

def get_default_country():
    try:
        return Country.objects.first().id
    except:
        return None