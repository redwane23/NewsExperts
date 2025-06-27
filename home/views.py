from django.shortcuts import render 
from .models import Profile
import requests
from decouple import config
import datetime
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse
from .serialiezer import NewsSerializer
import logging
from news import settings

logger = logging.getLogger(__name__)
def GetNews(catigory,search_date):

    api_key=config('NEWS_API_KEY')
    base_url_articals='https://newsapi.org/v2/everything'

    if search_date == 'yesterday':
        date=datetime.date.today() - datetime.timedelta(days=1)
    elif search_date == 'last week':
        date=datetime.date.today() - datetime.timedelta(days=7) 
    elif search_date == 'last mounth':
        date=datetime.date.today() - datetime.timedelta(days=30)

    params={'q': catigory,'from':date,'sortBy':'popularity',"apiKey":api_key}


    response=requests.get(base_url_articals,params=params)


    news_list=[]
    if response.status_code ==200:
        data=response.json()
        for  artical in data['articles']:
            image = artical.get('urlToImage')
            url = artical.get('url')
            if image and url:
                the_news={
                    'headline': artical['title'],
                    'text': artical['description'],
                    'image':image,
                    'pub_date':artical["publishedAt"],
                    'url':url,
                    }
                news_list.append(the_news)

    else:
        logger.error(f"News API Error: Status {response.status_code} - {response.text}")

        if settings.DEBUG:
            return JsonResponse({'error': 'Failed to fetch news', 'status': response.status_code, 'detail': response.text})
        else:
            return JsonResponse({'error': 'Unable to load news at the moment'}, status=503)
        
     

    return news_list
    
def GetTopNews():
    base_url_top_news='https://newsapi.org/v2/top-headlines'
    api_key=config('NEWS_API_KEY')
    params={
        'country':'us',
        'apiKey':api_key
    }
    response=requests.get(base_url_top_news,params=params)
    top_news_list=[]

    if response.status_code ==200:
        data=response.json()
        for  artical in data['articles']:
            image = artical.get('urlToImage')
            url = artical.get('url')
            if image and url:
                the_news={
                    'headline': artical['title'],
                    'text': artical['description'],
                    'image':image,
                    'pub_date':artical["publishedAt"],
                    'url':url,
                    }
                top_news_list.append(the_news)
    else:
        logger.error(f"News API Error: Status {response.status_code} - {response.text}")

        if settings.DEBUG:
            return JsonResponse({'error': 'Failed to fetch news', 'status': response.status_code, 'detail': response.text})
        else:
            return JsonResponse({'error': 'Unable to load news at the moment'}, status=503)
        

    

    return top_news_list

def GetWeather(profile):
    current_url= "http://api.weatherapi.com/v1/current.json"
    forecast_url = "http://api.weatherapi.com/v1/forecast.json"
    weather={}
    api_key = config('WEATHER_API_KEY')
    if profile:
        city=profile.City.name if profile.City else 'London'  
        
        params={'key':api_key ,  'q':f"{city}"}
        params2={'key':api_key ,  'q':f"{city}",'days':1}

        response=requests.get(current_url, params=params)
        response2=requests.get(forecast_url,params=params2 )

        current={}
        forecast={}

        if response.status_code ==200:
            data=response.json()

            current={
                'tempeture':data['current']['temp_c'],
                'description':data['current']['condition']['text'],
                'wind_kph':data['current']['wind_kph'],
                'humidity':data['current']['humidity'],
                'icon':data['current']['condition']['icon'],
                'location':data['location']["region"]
            }

        if response2.status_code == 200:
            data2=response2.json()
            forecast={
                'max_temp':data2['forecast']['forecastday'][0]['day']['maxtemp_c'],
                'min_temp':data2['forecast']['forecastday'][0]['day']['mintemp_c'],
                'avg_temp':data2['forecast']['forecastday'][0]['day']['avgtemp_c'],
                'humidity':data2['forecast']['forecastday'][0]['day']['avghumidity'],
                'rain':data2['forecast']['forecastday'][0]['day']['daily_will_it_rain'],
                'description':data2['forecast']['forecastday'][0]['day']['condition']['text'],
                'icon':data2['forecast']['forecastday'][0]['day']['condition']['icon'],
        }
        weather={'current':current,'forecast':forecast}
    else:
        logger.error(f"Weather API Error: Status {response.status_code} - {response.text}")

        if settings.DEBUG:
            return JsonResponse({'error': 'Failed to fetch weather', 'status': response.status_code, 'detail': response.text})
        else:
            return JsonResponse({'error': 'Unable to load weathe at the moment'}, status=503)
        
    return weather


class home(APIView):
    template_name = 'home/home.html'
    
    def get_context(self):
        user=self.request.user
        profile=Profile.objects.filter(user=user).first()

        return {
            'user':user,
            'profile':profile,
            'weather':GetWeather(profile),
            'top_news':GetTopNews(),
        }
    
    def get(self, request):
        context = self.get_context()
        return render(request, self.template_name, context)
    

class get_news(APIView):
    def paginate_news(self, request, news_list):
        paginator = PageNumberPagination()
        paginator.page_size = 15  
        page = paginator.paginate_queryset(news_list, request)
        return page
    
    def get_context(self,request,search_term=None):
        profile=Profile.objects.filter(user=self.request.user).first()
        if search_term:
            news=GetNews(search_term,profile.date_of_search)
        else:
            news=GetNews('world',profile.date_of_search)
        paginated_news = self.paginate_news(request,news)

        serialized_news=NewsSerializer(paginated_news,many=True).data
        return {
            "serialized_news":serialized_news,
        }
    
    def get(self,request):
        data=self.get_context(request)
        return JsonResponse(data)
        
        
    def post(self,request):
        search_term = request.POST.get('search_term')
        data=self.get_context(request,search_term)
        return JsonResponse(data)