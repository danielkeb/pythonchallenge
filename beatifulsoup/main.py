from bs4 import BeautifulSoup


import requests


respose=requests.get('http://news.ycombinator.com/news')

yc_we_page=respose.text

soup=BeautifulSoup(yc_we_page,'html.parser')
anchor_tags=soup.find_all(name="a", class_=".storylink")
print(anchor_tags.get())

article_text=[]
article_liks=[]
for article_ta in anchor_tags:
    text=article_ta.getText()
    article_text.append(text)
    link=article_ta.get("href")
    article_liks.append(link)

article_upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="upvote")]

largest_number=max(article_upvotes)
largest_index=article_upvotes.index(largest_number)














# with open('website.html', 'r') as html:
#     contents = html.read()



# soup= BeautifulSoup(contents,"html.parser")

# # print(soup.title.string)
# # print(soup.title.name)
# # print(soup.prettify())

# tags=soup.find_all(name="a")
# # for tag in tags:

# #     print(tag.get("href"))

# head=soup.select("#name")
# print(head)

# achortage=soup.select_one(selector="p a")
# print(achortage)

