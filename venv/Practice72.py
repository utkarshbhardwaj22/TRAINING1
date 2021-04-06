import requests
import json
import matplotlib.pyplot as plt

url = "https://api.covid19india.org/data.json"
response = requests.get(url)

covid_cases = json.loads(response.text)
#print(covid_cases)

statewise = covid_cases['statewise']
print(statewise)

cases = {}

for case in statewise:
    cases[case['state']] = int(case['active'])

print(cases)

for i,key in enumerate(cases):
    print(i,key,cases[key])
    plt.barh (key, cases[key])

plt.show()