#how to import this into the database
#how to separate start and end times
#get address information

import requests
from bs4 import BeautifulSoup
import re
import MySQLdb

gmap = {}

#wednesday
url = "http://www.therooster.com/happyhours/boulder#d=wednesday"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

wedInfo = soup.find_all("div", {"class" : "details"})
i = 0
for item in wedInfo:
	try:
		restname = item.contents[1].text
		gmap[i] = restname
	except:
		print "got an error"
	wedTime = item.contents[5].find_all("div", {"class" : "time"})[0].text
	wedDrinks = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[0].text.replace('Drinks:', '')
	try:
		wedFood = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[1].text.replace('Food:', '')
	except:
		pass
	i=i+1

for key in gmap.keys():
	print key,gmap[key]
	key = str(key)
	conn = MySQLdb.connect(user="root",db="HappyApp")
	query = "INSERT INTO Restaurant (restName,restID) values ("
	query = query+"'"+key+"',"+gmap[key]+")"
	x = conn.cursor()
	x.execute(query)
	row = x.fetchall()

