import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/table/series/8048/season/2019/indian-premier-league"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

teamTags=soup.find_all("span",class_="team-names")
# mTags=soup.find_all("td",attrs={"data-reactid":"279"})
mTags=soup.find_all("td",class_="")
teams=[]
matches=[]

for tag in teamTags:
    teamTitle=tag.text.strip()
    teams.append(teamTitle)

for matchesTag in mTags:
    totalMatch=matchesTag.text.strip()
    matches.append(totalMatch)

print(teams)
# for match in matches:
print(matches)