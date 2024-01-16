import requests
import smtplib
STOCK_NAME = "TSLA"
my_key_stock="JE47QYQDO7VT0K5X"
COMPANY_NAME = "Tesla Inc"
url="https://www.alphavantage.co/query"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameters ={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":"IBM",
    "apikey":"demo"
}
news_key="3b3e81af9f8c425bac0d43f8e76f7c41"
response=requests.get(STOCK_ENDPOINT,params=parameters)

data=response.json()

stock_data=data["Time Series (Daily)"]

data_list=[value for (key, value)in stock_data.items()]

yesterday_close_price=float(data_list[0]['4. close'])
before_yesterday_close_price=float(data_list[1]['4. close'])
print(yesterday_close_price, before_yesterday_close_price)

difference=yesterday_close_price - before_yesterday_close_price

if difference<0:
    updown=""
else:
    updown=""

#prcentage of the difference

df_percent=round(difference / yesterday_close_price *100)

print(df_percent)

news_parameters={
    'q':'apple',
    'from':'2024-01-15',
    'to':'2024-01-15',
    'sortBy':'popularity',
    'apiKey':news_key
}


if abs(df_percent) >1:
    print("Great News")
    new_api=requests.get(NEWS_ENDPOINT, params=news_parameters)
    new_api.raise_for_status()
    news_data=new_api.json()
   # print("title")
    articles=news_data['articles']
    three_articles=articles[:3]
   # print(three_articles)
    articles_news=[f"Headline:{updown}{df_percent}% {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]
    connection=smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="dantera830@gmail.com", password="5345SFYDYTRTASS")
    for news in articles_news:
        connection.sendmail(
            from_addr="danter830@gmail.com", 
            to_addrs="danielkebede381@gmail.com",
            
            msg=f"Subject:News!\n\n {news}")


   #print(three_articles[0]["description"])

   # print(news_data['articles'][:2]['description'])

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

