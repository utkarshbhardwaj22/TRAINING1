import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/ipl-2020-21-1210595/points-table-standings"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

team_name_tags = soup.find_all("h5", class_= "header-title label")
team_name = []

for tag in team_name_tags:
    #print(tag.text.strip())
    team_name.append(tag.text.strip())

del team_name[0]

print("{} teams for IPL 2020".format(len(team_name)))
print(team_name)

team_data_tags = soup.find_all("td", class_="")
team_data = []

for i in range(len(team_name)):
    team_data.append([])

i = 0
j = 0
for tag in team_data_tags:
    #print(tag.text.strip())
    team_data[i].append(tag.text.strip())
    j += 1

    if j%7 == 0:
        print("Team {} data entered".format(i))
        i += 1

print(team_data)

team_points_tags = soup.find_all("td", class_ = "border-right label")
team_points = []
for tag in team_points_tags:
    #print(tag.text.strip())
    team_points.append(tag.text.strip())

print(team_points)

print("TEAM WISE DETAILS:")
print("**************************************************")
for i in range(len(team_name)):
    print("======================================")
    print(team_name[i])
    print(team_data[i])
    print(team_points[i])
    print("======================================")
    print()