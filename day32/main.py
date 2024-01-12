import pandas as pd
from datetime import datetime
import random
import smtplib
data=pd.read_csv("birthdays.csv")

today=datetime.now()
day_tuple=(today.month, today.day)

new_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
my_email="dantera830@gmail.com"
password="qvfxozjdpovcxncb"
if day_tuple in new_dict:
    birth_person=new_dict[day_tuple]
    file_path=f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as ltr:
        txt=ltr.read()
        message=txt.replace("[NAME]", birth_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birth_person["email"],
            msg=f"Subject:Happy birthday\n\n{message}")

