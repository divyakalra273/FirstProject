import requests
from bs4 import BeautifulSoup
import pandas as pd


class Team:
    def __init__(self,year, teamName, matches, won, lost, tied, abandoned, points, netRunRate, forScore, againstScore):
        self.year=year
        self.teamName = teamName
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abandoned = abandoned
        self.points = points
        self.netRunRate = netRunRate
        self.forScore = forScore
        self.againstScore = againstScore

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{}\n".format(self.year,self.teamName, self.matches, self.won, self.lost, self.tied,
                                                        self.abandoned, self.points, self.netRunRate, self.forScore,
                                                        self.againstScore)

class FetchingData:
    def fetchData(self,year):
        url = "https://www.espncricinfo.com/table/series/8048/season/{}/ipl".format(year)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        teamNameTags = soup.find_all("span", class_="team-names")
        teamDataTags = soup.find_all("td", class_="")
        iplTeamsNames = []
        iplTeamsData = []
        for tag in teamNameTags:
            print(tag.text.strip())
            iplTeamsNames.append(tag.text.strip())
            iplTeamsData.append([])
        i = 0
        j = 0
        for tag in teamDataTags:

            print(tag.text.strip())
            try:

                iplTeamsData[j].append(int(tag.text.strip()))
            except Exception as e:
                iplTeamsData[j].append(tag.text.strip())

            i += 1
            if i % 9 == 0:
                j += 1
                print("~~~~~~~~")

        print(iplTeamsNames)
        print(iplTeamsData)


        teams = []
        for i in range(0, len(iplTeamsNames)):
            team = Team(year,iplTeamsNames[i], iplTeamsData[i][0], iplTeamsData[i][1], iplTeamsData[i][2], iplTeamsData[i][3], iplTeamsData[i][4], iplTeamsData[i][5], iplTeamsData[i][6], iplTeamsData[i][7], iplTeamsData[i][8])
            teams.append(team)


        file = open("IPL-TEAMS-2019.csv", "a")

        for team in teams:
            print(team)
            data = str(team)
            file.write(data)


        print("--CSV FILE GENERATED--")

def main():
    print("==App Started==")

    # fRef = FetchingData()
    # years = list(range(2008, 2020, 1))
    # for year in years:
    #     fRef.fetchData(year)

    print("==App Finished==")

    table = pd.read_csv("IPL-TEAMS-2019.csv")
    print(table)
    for i in range(1,101):
        name = table.loc[i][1]
        wins = table.loc[i][3]

        print(name)
        print(wins)

if __name__ == "__main__":
    main()