- NewsExperts
* Description

A Django and based platform that displays real-time news and weather updates based on user location,
with features like profile management, to-do tracking,map integrations to choose any city in the db.

* Features

1- Fetches and displays news and weather based on user input (location and category)
2- Map integration with Leaflet.js  
3- Profile system to hold user info and change it
4- To-do list with CRUD operations  
5- Responsive UI (mobile/tablet friendly) made with figma
6- choos city from the map by one click(self made function)

* Tech used

- django
- django rest framwork
- leaflit map
- third party pai(weatherapi,newsapi)
- cities_light package for all world cities
- figma

*  Installation Instructions

1. Clone the repo
   git clone ("https://github.com/redwane23/NewsExperts/")

2. Backend Setup
   cd backend
   pip install -r requirements.txt
   python mange.py makemigraions
   python manage.py migrate
   
4.adding the env variabals
  create a .env file
    NEWS_API_KEY="YOUR NEWS API KEY" =>  [[newsapi] (https://newsapi.org/docs/get-started)](https://newsapi.org/docs/get-started)
    WEATHER_API_KEY="YOUR WEATHER API KEY" =>   [weatherapi](https://www.weatherapi.com/docs/)

5. open on localhost
  python manage.py runserer
  http://127.0.0.1:8000/home/world/

author
  Redwane — [LinkedIn](https://linkedin.com/in/yourprofile)



