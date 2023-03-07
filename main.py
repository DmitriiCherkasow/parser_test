import requests
from APIKey import API_TOKEN

params = {"q": "Самара", "appid": API_TOKEN, "units": "metric"}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

x = response.json()

print(x)

