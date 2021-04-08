import requests
from bs4 import BeautifulSoup



class Team:
    def __init__(self, name, matches, won, lost, points, nrr):
        self.name = name
        self.matches = matches
        self.won = won
        self.lost = lost
        self.points = points
        self.nrr = nrr

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.name, self.matches, self.won, self.lost, self.points, self.nrr)

class FetchTeamData:

    def fetch_data(self):
        url = "https://www.espncricinfo.com/series/ipl-2020-21-1210595/points-table-standings"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")

        team_name_tags = soup.find_all("h5", class_="header-title label")
        team_name = []

        for tag in team_name_tags:
            # print(tag.text.strip())
            team_name.append(tag.text.strip())

        del team_name[0]



        team_data_tags = soup.find_all("td", class_="")
        team_data = []

        for i in range(len(team_name)):
            team_data.append([])

        i = 0
        j = 0
        for tag in team_data_tags:
            # print(tag.text.strip())
            team_data[i].append(tag.text.strip())
            j += 1

            if j % 7 == 0:

                i += 1



        team_points_tags = soup.find_all("td", class_="border-right label")
        team_points = []
        for tag in team_points_tags:
            # print(tag.text.strip())
            team_points.append(tag.text.strip())



        teams = []

        for i in range(len(team_name)):
            print("======================================")
            print(team_name[i])
            print(team_data[i])
            print(team_points[i])
            print("======================================")
            print()
            for i in range(len(team_name)):

                team = Team(
                    name= team_name[i],
                    matches= team_data[i][0],
                    won= team_data[i][1],
                    lost= team_data[i][2],
                    points= team_points[i],
                    nrr= team_data[i][4]

                )

                teams.append(team)

            return teams

class DataSetGenrator:

    def list_to_file(self,file_name, data):
        file = open(file_name, "a")
        for line in data:
            file.write(str(line))

        print("DataSet Generated.")

def main():

    fetchTask = FetchTeamData()
    teams = fetchTask.fetch_data()

    for team in teams:
        print(team)

    ds_gen = DataSetGenrator()
    ds_gen.list_to_file(file_name="Ipl Points Table.csv", data=teams)


if __name__ == '__main__':
    main()

