import smtplib
import requests
from  datetime import datetime

# MY_LONGITUDE=87.31197425
# MY_LATITUDE=23.0478115
# response=requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data=response.json()
# latitude=data["iss_position"]["latitude"]
# longitude=data["iss_position"]["longitude"]
# iss_position=(latitude,longitude)
# print(iss_position)
# parameters={
#     "lat": MY_LATITUDE,
#     "lng":MY_LONGITUDE,
#     "formatted":0
# }
# response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
# response.raise_for_status()
# data=response.json()
# sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)
# time_now=datetime.now()
# print(time_now.hour)

import smtplib
from datetime import datetime
import requests
import time
MY_LONGITUDE=87.31197425
MY_LATITUDE=23.0478115
my_email = "prithwishpatra05@gmail.com"
password = "jmqjjqzrpheixcaj"
def is_iss_overhead():
    iss_pos=requests.get("http://api.open-notify.org/iss-now.json")
    iss_pos.raise_for_status()
    iss_data=iss_pos.json()
    latitude=iss_data["iss_position"]["latitude"]
    longitude=iss_data["iss_position"]["longitude"]
    if MY_LONGITUDE-5<=longitude<=MY_LONGITUDE+5 and MY_LATITUDE-5<=latitude<=MY_LATITUDE+5:
        return True
def is_night():
    parameters={
        "lat": MY_LATITUDE,
        "lng":MY_LONGITUDE,
        "formatted":0
    }
    response=requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    sun_data=response.json()
    sunrise=sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=sun_data["results"]["sunset"].split("T")[1].split(":")[0]
    time_now=datetime.now()
    if time_now>=sunset or time_now <=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="padmapatra1986@gmail.com",
            msg="Subject:LOOK UP\n\n The ISS is above you in the sky"
        )