#how to import this into the database
#how to separate start and end times
#get address information

import requests
from bs4 import BeautifulSoup
import re
import MySQLdb


gmap = {}

#tuesday
url = "http://www.therooster.com/happyhours/boulder#d=tuesday"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

tueInfo = soup.find_all("div", {"class" : "details"})
i = 0
for item in tueInfo:
	try:
		restname = item.contents[1].text
		gmap[i] = restname
	except:
		print "got an error"
	tueTime = item.contents[5].find_all("div", {"class" : "time"})[0].text
	tueDrinks = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[0].text.replace('Drinks:', '')
	try:
		tueFood = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[1].text.replace('Food:', '')
	except:
		pass
	i=i+1

addrest = ("INSERT INTO Restaurant"
			  "(restname, address)" 
			  "VALUES (%s, %s)")



conn = MySQLdb.connect(user="root",db="mydb")
x = conn.cursor()

for key in gmap.keys():
	print gmap[key]	
	name = gmap[key]
	add = "temp"
	datarest = (str(name),str(add))
	x.execute(addrest, datarest)
x.close()
conn.commit()
conn.close()
