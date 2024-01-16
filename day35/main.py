import requests 
#from twilio.rest import Client
key="b4e7309ca871dcb4e94816271c5da910"
LAT=51.507351
LONNG=-0.127758
MY_KEY='a69bd5e84b6694abf08c7409da6af0f8'
parameters={
    "lat":LAT,
    "lon":LONNG,
    "appid":key,
    "exclude":"current,minutely,daily",
}



response = requests.get("https://api.openweathermap.org/data/2.5/onecall/",params=parameters)

# response=requests.get("https://api.openweathermap.org/data/2.5/weather?q=london,%20UK&appid=7fd2018c3c2ac649a104797c39ecc11b")
response.raise_for_status()
data=response.json()
print(data)
# weather_data = data['hourly'][:11]

# will_rain=False
# for hour in weather_data:
#     weather_coditio=hour['weather'][0]['id']
#     if weather_coditio <700:
#         will_rain=True
#     else:
#         will_rain=False

# if will_rain:
#     account_sid=''
#     auth_token=''
#     client=Client(account_sid, auth_token)
#     message=client.messages\
#     .create(
#         body="take umbrella it will rain later",
#         from_='+25194234234',
#         to='+251942343',
#     )