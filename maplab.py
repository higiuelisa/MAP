from dotenv import load_dotenv
import os
import requests

load_dotenv()

cheie_api_openweather=os.getenv("API_KEY")

url= "https://api.openweathermap.org/data/2.5/weather?"

raspuns= requests.get(url, params={
    'lat': 46.566881,
    'lon':26.898324,
    'appid': cheie_api_openweather
    }).json()
#print (raspuns)


url_geocoding ="https://api.openweathermap.org/geo/1.0/direct?"
lat=raspuns_geocoding[0]['lat']
lat=raspuns_geocoding[0]['lon']
rapuns_geocoding = requests.get(url_geocoding, params={
    'lat': lat,
    'lon':lon,
    'appid': cheie_api_openweather,
    'units':'metric',
    'lang':'ro'
    
})

starea_vremii=raspuns['weather'][0]['description']
temperatura = raspuns['main']['temp']
viteza_vant = raspuns['wind']['speed']

print(f"In {oras} sunt {temperatura} grade")

#print(cheie_api_openweather)
