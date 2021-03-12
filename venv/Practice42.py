import requests
import json

api_key = "your api key"
url = "http://newsapi.org/v2/everything?q=tesla&from=2021-02-12&sortBy=publishedAt&apiKey={}".format(api_key)
response = requests.get(url)
print(response.text)
print(type(response.text))

dict_data = json.loads(response.text)
print(dict_data)
print(type(dict_data))