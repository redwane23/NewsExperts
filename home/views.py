from django.shortcuts import render 
from .models import Profile
import requests
from django.contrib.auth.decorators import login_required
from decouple import config

def GetNews(catigory):
    api_key=config('NEWS_API_KEY')
    base_url_articals='https://newsapi.org/v2/everything'
    base_url_top_news='https://newsapi.org/v2/top-headlines'

    params={'q': catigory,'from':'2025-01-01','sortBy':'popularity',"apiKey":api_key}
    params2={
        'country':'us',
        'apiKey':api_key
    }

    response=requests.get(base_url_articals,params=params)
    response2=requests.get(base_url_top_news,params=params2)

    news_list=[]
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
                news_list.append(the_news)

    else:
        print('faild to load content 1')
        print(response.status_code)
    
    if response2.status_code ==200:
        data=response2.json()
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
        print('faild to load content 2')
        print(response2.status_code)



    return news_list,top_news_list

def GetWeather(profile):
    current_url= "http://api.weatherapi.com/v1/current.json"
    forecast_url = "http://api.weatherapi.com/v1/forecast.json"

    api_key = config('WEATHER_API_KEY')
    city=profile.City
    
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

    return weather

@login_required
def home(request,catigory):
    user=request.user
    profile=Profile.objects.get(User=user)

    if request.method=='POST':
        search_term=request.POST.get("search_term")
        news,top_news_list=GetNews(search_term)
    else:
        news,top_news_list=GetNews(catigory)
    weather=GetWeather(profile)

    context={
        'user':user,
        'profile':profile,
        'news':news,
        'top_news_list':top_news_list,
        'weather':weather,
    }
    return render(request,'home/home.html',context)