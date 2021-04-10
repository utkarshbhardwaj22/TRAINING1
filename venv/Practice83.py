import requests
import json
import pandas as pd

url = "https://api.covid19india.org/data.json"

response = requests.get(url)

covid_data = json.loads(response.text)
#print(covid_data)

statewise_covid_data = pd.DataFrame(covid_data['statewise'])
print(statewise_covid_data)

print("STATES")
print(statewise_covid_data.state)
print()
print("ACTIVE CASES")
print(statewise_covid_data.active)


