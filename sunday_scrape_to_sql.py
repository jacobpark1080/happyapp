#figure out what to do with multiple stimes and etimes
#get address information


import requests
from bs4 import BeautifulSoup
import re
import MySQLdb


gmap = {}
timemap = {}
drinkmap = {}
foodmap = {}
#Sunday
url = "http://www.therooster.com/happyhours/boulder#d=sunday"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

Info = soup.find_all("div", {"class" : "details"})
i = 0
for item in Info:
	try:
		restname = item.contents[1].text
		gmap[i] = restname
	except:
		print "got an error"
	timemap[i] = item.contents[5].find_all("div", {"class" : "time"})[0].text
	drinkmap[i] = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[0].text.replace('Drinks:', '')
	try:
		foodmap[i] = item.contents[5].find_all("div", {"class" : "foods"})[0].find_all("div", {"class": "food"})[1].text.replace('Food:', '')
	except:
		pass
	i=i+1

add_special = ("INSERT INTO Sunday" 
			"(Restaurant_restname, stime, etime,food,drink)"
			"VALUES (%s, %s, %s, %s, %s)")
addrest = ("INSERT INTO Restaurant"
			  "(restname, address)" 
			  "VALUES (%s, %s)")


conn = MySQLdb.connect(user="root",db="mydb")
x = conn.cursor()

for key in gmap.keys():
	
	name = gmap[key]
	add = "temp"
	try:
		x.execute(addrest, datarest)
	except:
		pass

	time = timemap[key]
	drink = drinkmap[key]
	drink = drink.encode('ascii','ignore')
	Drinks = drink.replace('/n', '')
	Drinks = Drinks.replace('[ ]\+', '')
	try:
		food = foodmap[key]
		food = food.encode('ascii','ignore')
		Foods = food.replace('/n', '')
		Foods = Foods.replace('[ ]\+', '')
	except:
		pass
	
	time = time.split('-',1)
	stime = time[0]
	try:
		etime = time[1]
	except:
		stime = "0:00"
		etime = "24:00"
	st = stime.replace("pm","")	
	st = st.replace(":00"," ")
	st = st.replace(":30",".5")
	et = etime.replace("pm","")
	et = et.replace(":00"," ")
	et = et.replace(":30",".5")
	
	data_special = (str(name), str(st), str(et), str(Drinks), str(Foods))
	try:
		x.execute(add_special,data_special)
	except:
		pass

x.close()
conn.commit()
conn.close()
