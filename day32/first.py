import smtplib
import datetime as dt
import random
now=dt.datetime.now()

date_of_birth=dt.datetime(month=9, day=11, year=2000, hour=3)
print(date_of_birth)

today=now.weekday()
print(today)

# if today == 3:
#     with open("quotes.txt") as f:
#         content=f.readlines()
#     qoute=random.choice(content)

#     my_email="dantera830@gmail.com"
#     password="qvfxozjdpovcxncb"

#     #qvfxozjdpovcxncb
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password= password)
        
#         connection.sendmail(
#             from_addr=my_email, 
#             to_addrs="danielkebede824@yahoo.com", 
#             msg=f"Subject:Motivation from monday qoutes\n\n{qoute}.")


