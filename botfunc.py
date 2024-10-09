import requests
from pyfiglet import Figlet
import os, time

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

def postcode_fetcher(postcode):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()
    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    return [area, longitude, latitude]

def cat_facts():
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    return joke

def weather_fetcher(lat, lon):
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=4d30afa58f6f935d861edecad3639cda").json()
    # print(weather_resp)
    weather_kelvin = weather_resp["main"]["temp"]
    # convert to degrees
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    return [weather_degrees, main_weather_desc, second_weather_desc]