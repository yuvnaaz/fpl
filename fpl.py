from bs4 import BeautifulSoup
import pandas as pd
import requests

START_URL = "https://fantasy.premierleague.com/statistics"
page = requests.get(START_URL, verify=False)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table")
body = table.find("tbody")

form = []
pts = []
sel = []
player = []
cost = []

for tr_tag in body.find_all("tr"):
    td_tags = tr_tag.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    player.append(row)

for i in range(1, len(player)):
    player.append(Player[i][1])
    sel.append(Selected[i][3])
    cost.append(Cost[i][5])
    pts.append(Points[i][6])

dict = {"Player": player, "Form": form, "Points": pts, "Cost": cost, "Selected": sel}
df = pd.DataFrame(dict)
df.to_csv("fpl.csv")