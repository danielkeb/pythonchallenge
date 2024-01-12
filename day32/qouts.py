import random
import smtplib
import datetime as dt
with open("quotes.txt", "r") as qout:
    content=qout.readlines()
    


qoute=random.choice(content)
now=dt.datetime.now()
moday=now.weekday()
if moday==3:
    my_email="dantera380@gmail.com"
    password="qvfxozjdpovcxncb"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password= password)
            
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="danielkebede824@yahoo.com", 
                msg=f"Subject:Motivation from monday qoutes\n\n{qoute}.")