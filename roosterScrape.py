#how to import this into the database
#how to separate start and end times
#get address information

import requests
from bs4 import BeautifulSoup
import re

#wednesday
url = "http://www.therooster.com/happyhours/boulder#d=wednesday"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

info = soup.find_all("div", {"class" : "details"})
for item in info:
	restName = item.contents[1].text
	time = item.contents[5].find_all("div", {"class" : "time"})[0].text
	drinks = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[0].text.replace('Drinks:', '')
	try:
		food = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[1].text.replace('Food:', '')
	except:
		pass

	
