
from rest_framework import serializers
from Profile.models import Task,TaskList
from cities_light.models import Country,City

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
class CitySerializers(serializers.ModelSerializer):

    country_name = serializers.CharField(source='country.name', read_only=True)
    region_name = serializers.CharField(source='region.name', read_only=True)
    class Meta:
        model= City
        fields='__all__'