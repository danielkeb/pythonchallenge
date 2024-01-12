import smtplib
import requests
from datetime import datetime
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT -5 <=iss_latitude and MY_LAT +5 and MY_LONG -5 <=iss_longitude  <=MY_LONG +5:
        return True
def is_nignt():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])

    time_now = datetime.now().hour
    print(type(time_now))
    if time_now>=sunset or time_now <=sunrise:
        return True
    while True:
        time.sleep(60)
        if is_iss_overhead() and is_nignt():
            conn=smtplib.SMTP("smtp.gmail.com")
            conn.starttls()
            conn.login( user="danter830@gmail.com", password="5345SFYDYTRTASS")
            conn.sendmail(
                from_addr="danter830@gmail.com",
                to_addrs="danielkebede381@gmail.com",
                msg="Subject:Look Up\n\nThe ISS is above you in the sky.")
       



is_iss_overhead()
is_nignt()