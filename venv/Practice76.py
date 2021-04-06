"""
Beautiful Soup -> Web Scrapping

"""
import requests
from bs4 import BeautifulSoup

url= "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

movie_name_tags = soup.find_all(class_= "loadlate")

for tag in movie_name_tags:
    print(tag)