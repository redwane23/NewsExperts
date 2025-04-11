from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from Profile.models import TaskList,CountryList
from django.contrib.auth.models import User


@receiver(post_save,sender=User)
def my_callback(sender,instance,created ,**kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            FirstName=instance.first_name,
            LastName=instance.last_name,
            Email=instance.email,
            )
        TaskList.objects.create(
            owner=instance,
        )
        CountryList.objects.create(
            owner=instance,
        )