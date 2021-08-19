import requests
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/leagues/NBA_2021_leaders.html"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find("div" ,{"class" : "data_grid"})


pts = list.find("div",{"id" : "leaders_pts"}).text
print(pts)

ptsperg = list.find("div",{"id" : "leaders_pts_per_g"}).text
print(ptsperg)

trb = list.find("div",{"id" : "leaders_trb"}).text
print(trb)







    