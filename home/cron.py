import requests
from decouple import config
import datetime
from django.http import JsonResponse
import logging
from news import settings

from django.core.cache import cache
logger = logging.getLogger(__name__)

def refresh_news_cache():
    api_key=config('NEWS_API_KEY')
    base_url_articals='https://newsapi.org/v2/everything'

    Dates=[
        datetime.date.today() - datetime.timedelta(days=1),
        datetime.date.today() - datetime.timedelta(days=7),
        datetime.date.today() - datetime.timedelta(days=30)
    ]

    Parameters={f"params{i+1}":{'q': 'world','from':Dates[i],'sortBy':'popularity',"apiKey":api_key} for i in range(3)}
    Responses={f"response{i+1}": requests.get(base_url_articals,params=Parameters[f"params{i+1}"]) for i in range(3)}
    NewsList={f"NewsList{i+1}":[] for i in range(3)}

    for i in range(3):
        response=Responses[f'response{i+1}']
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
                    NewsList[f'NewsList{i+1}'].append(the_news)

                    cache_key=f"news_world_{i+1}"

                    cache.set(cache_key,NewsList[f'NewsList{i+1}'], timeout=60 * 60)
            print(f"News for category {i+1} cached successfully.")

        else:
            logger.error(f"News API Error: Status {f"response{i+1}".status_code} - {response.text}")

            if settings.DEBUG:
                return JsonResponse({'error': 'Failed to fetch news', 'status': response.status_code, 'detail': Responses[f'response{i+1}'].text})
            else:
                return JsonResponse({'error': 'Unable to load news at the moment'}, status=503)