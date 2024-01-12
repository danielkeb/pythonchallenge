import requests
from datetime import datetime
latitude=51.507351
longitude=-0.127758


paramaters={
    "lat":latitude,
    "lng":longitude,
    "formatted":0,
    }
response= requests.get("https://api.sunrisesunset.io/json", params=paramaters)

response.raise_for_status()
data=response.json()
sunrise=data['results']["sunrise"]
sunset=data['results']["sunset"]
print(sunrise.split(":")[0])
print(sunset.split(":")[0])


time=datetime.now()
print(time.hour)