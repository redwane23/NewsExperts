
from rest_framework import serializers
from Profile.models import Task,TaskList
from cities_light.models import Country

class TaskListSerializers(serializers.ModelSerializer):
    class Meta:
        model= TaskList
        fields=('__all__')


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields=('__all__')

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model= Country
        fields=('__all__')
