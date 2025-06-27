from rest_framework import generics
from Profile.models import TaskList,Task
from .serializers import TaskListSerializers,TaskSerializers,CitySerializers
from rest_framework.response import Response
import math
from geopy.distance import geodesic
from cities_light.models import City
from django.http import JsonResponse


class TaskListView(generics.ListAPIView):
    serializer_class=TaskListSerializers

    def get_queryset(self):
        queryset=TaskList.objects.all()
        return queryset

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializers
    queryset=Task.objects.all()

class TaskCreation(generics.CreateAPIView):

    serializer_class=TaskSerializers

class ResetTasks(generics.GenericAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializers

    def delete(self,request):
        list_id=request.query_params.get('list')
        if list_id is not None:
                queryset=self.queryset.filter(list=list_id)
                deleted_count, _ = queryset.delete()
                return Response({'message':'deleted sucssefully'})

        queryset=self.queryset.filter(list=list_id)
        deleted_count, _ = queryset.delete()
        return Response({'message':'invalid list id'})

def getcity(request,lat,lng):
    
    max_distance=100 #max distance between clicked button and the nearext city

    lat_diff= max_distance/111
    lng_diff= max_distance/(111*math.cos(math.radians(lat)))

    lat_min=lat-lat_diff
    lat_max=lat+lat_diff
    lng_min=lng-lng_diff
    lng_max=lng+lng_diff

    cities=City.objects.filter(latitude__gte=lat_min,latitude__lte=lat_max,longitude__gte=lng_min,longitude__lte=lng_max)


    if cities:
        nearest_city=None
        min_dist=float('inf')

        for city in cities:
            city_coords = (city.latitude,city.longitude)
            distance = geodesic((lat,lng),city_coords).kilometers
            if distance<min_dist:
                nearest_city=CitySerializers(city).data
                min_dist=distance
        data={
            'status':'success',
            'city':nearest_city,
        }
        return JsonResponse(data)

    data={
        'status':'failed',
        'city_id':0,
        'city_name':'No city found within the 100km distance.'
    }
    return  JsonResponse(data)
                